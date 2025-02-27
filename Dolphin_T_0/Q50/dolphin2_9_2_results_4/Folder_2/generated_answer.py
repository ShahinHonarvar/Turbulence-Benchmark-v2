def if_contains_anagrams(strings):
    anagram_pairs = set()
    for string in strings:
        if len(string) >= 3:
            string = string.lower()
            sorted_string = ''.join(sorted(string))
            anagram_pairs.add(sorted_string)
    return len(anagram_pairs) >= 246