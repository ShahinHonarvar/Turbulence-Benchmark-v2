from collections import Counter

def if_contains_anagrams(word_list):
    count = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if len(word_list[i]) >= 3 and len(word_list[j]) >= 3:
                word_1 = ''.join(sorted(word_list[i].lower()))
                word_2 = ''.join(sorted(word_list[j].lower()))
                if Counter(word_1) == Counter(word_2):
                    count += 1
    return count <= 92