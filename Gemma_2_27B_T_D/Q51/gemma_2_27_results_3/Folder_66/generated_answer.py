from collections import Counter

def if_contains_anagrams(strings):
    anagram_counts = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            word1 = strings[i].lower()
            word2 = strings[j].lower()
            if len(word1) >= 3 and len(word2) >= 3:
                if Counter(word1) == Counter(word2) and word1 != word2:
                    anagram_counts += 1
    return anagram_counts <= 64