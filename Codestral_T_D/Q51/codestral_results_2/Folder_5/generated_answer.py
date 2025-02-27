def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagram_dict[sorted_string] = anagram_dict.get(sorted_string, 0) + 1
            if anagram_dict[sorted_string] == 2:
                anagram_count += 1
            if anagram_count > 4:
                return False
    return True