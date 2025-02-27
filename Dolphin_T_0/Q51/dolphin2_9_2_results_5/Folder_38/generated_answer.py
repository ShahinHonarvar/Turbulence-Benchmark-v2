from collections import Counter

def if_contains_anagrams(word_list):
    count = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            word1 = word_list[i].lower()
            word2 = word_list[j].lower()
            if len(word1) >= 3 and len(word2) >= 3:
                if Counter(word1) == Counter(word2):
                    count += 1
    return count <= 416