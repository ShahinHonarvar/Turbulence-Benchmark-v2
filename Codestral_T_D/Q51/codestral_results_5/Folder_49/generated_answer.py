from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    anagrams = {}
    for s in strings:
        s = s.lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
            anagram_count += len(anagrams[sorted_s]) - 1
            if anagram_count > 10:
                return False
        else:
            anagrams[sorted_s] = [s]
    return True