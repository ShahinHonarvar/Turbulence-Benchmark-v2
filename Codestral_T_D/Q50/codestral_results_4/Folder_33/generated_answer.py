from collections import Counter

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for s in strings:
        s = s.lower()
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagram_dict:
                anagram_count += anagram_dict[sorted_s]
                anagram_dict[sorted_s] += 1
            else:
                anagram_dict[sorted_s] = 1
    return anagram_count >= 140