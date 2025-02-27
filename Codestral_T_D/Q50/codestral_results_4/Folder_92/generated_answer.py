def if_contains_anagrams(strings):
    anagram_dict = {}
    for string in strings:
        lowercase_string = string.lower()
        if len(lowercase_string) < 3:
            continue
        sorted_string = ''.join(sorted(lowercase_string))
        if sorted_string in anagram_dict:
            return True
        anagram_dict[sorted_string] = lowercase_string
    return False