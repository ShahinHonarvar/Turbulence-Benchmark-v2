from collections import Counter

def if_contains_anagrams(lst):
    count_anagrams = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            word1 = lst[i].lower()
            word2 = lst[j].lower()
            if len(word1) >= 3 and len(word2) >= 3 and (Counter(word1) == Counter(word2)):
                count_anagrams += 1
    return count_anagrams >= 66