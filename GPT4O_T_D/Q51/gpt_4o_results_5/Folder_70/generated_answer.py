from collections import Counter

def if_contains_anagrams(strings):
    anagram_signatures = {}
    count_anagram_pairs = 0
    for s in strings:
        if len(s) >= 3:
            normalized_str = ''.join(filter(str.isalpha, s)).lower()
            signature = ''.join(sorted(normalized_str))
            if signature in anagram_signatures:
                count_anagram_pairs += anagram_signatures[signature]
                anagram_signatures[signature] += 1
            else:
                anagram_signatures[signature] = 1
    return count_anagram_pairs <= 97