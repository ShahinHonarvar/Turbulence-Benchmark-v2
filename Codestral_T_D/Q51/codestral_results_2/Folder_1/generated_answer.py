def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_dict[sorted_string] = anagram_dict.get(sorted_string, 0) + 1
        if anagram_dict[sorted_string] >= 2:
            anagram_count += 1
            if anagram_count > 30:
                return False
    return True