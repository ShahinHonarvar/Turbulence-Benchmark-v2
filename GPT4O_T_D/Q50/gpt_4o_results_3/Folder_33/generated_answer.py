from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    n = len(strings)
    normalized_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    for i in range(n):
        for j in range(i + 1, n):
            if len(normalized_strings[i]) >= 3 and normalized_strings[i] == normalized_strings[j]:
                anagram_count += 1
                if anagram_count >= 140:
                    return True
    return False