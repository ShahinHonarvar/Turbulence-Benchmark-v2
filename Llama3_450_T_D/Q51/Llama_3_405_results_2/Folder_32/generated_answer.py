def if_contains_anagrams(strings):
    anagram_dict = {}
    count = 0
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3 and sorted_str in anagram_dict and all((c.isalpha() for c in s)):
            count += anagram_dict[sorted_str]
            anagram_dict[sorted_str] += 1
        else:
            anagram_dict[sorted_str] = 1
    return count <= 89