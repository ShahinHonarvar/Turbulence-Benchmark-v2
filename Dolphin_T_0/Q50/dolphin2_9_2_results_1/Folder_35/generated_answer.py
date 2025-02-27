from collections import Counter

def if_contains_anagrams(word_list):
    n = len(word_list)
    anagram_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if len(word_list[i]) < 3 or len(word_list[j]) < 3:
                continue
            if Counter(sorted(word_list[i])) == Counter(sorted(word_list[j])).lower():
                anagram_pairs += 1
                if anagram_pairs >= 153:
                    return True
    return False