from collections import Counter

def if_contains_anagrams(lst):
    anagrams = 0
    for i in range(len(lst)):
        word1 = lst[i]
        for j in range(i + 1, len(lst)):
            word2 = lst[j]
            if len(word1) >= 3 and len(word2) >= 3 and (Counter(word1.lower()) == Counter(word2.lower())):
                anagrams += 1
    return anagrams >= 36