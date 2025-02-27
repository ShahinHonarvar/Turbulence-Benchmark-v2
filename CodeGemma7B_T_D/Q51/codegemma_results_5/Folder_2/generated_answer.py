def if_contains_anagrams(str_list):
    anagram_lookup = {}
    for word in str_list:
        key = ''.join(sorted(word, key=str.casefold))
        if len(word) >= 3 and key not in anagram_lookup:
            anagram_lookup[key] = word
            if len(anagram_lookup) == 81:
                return True
    return len(anagram_lookup) <= 81