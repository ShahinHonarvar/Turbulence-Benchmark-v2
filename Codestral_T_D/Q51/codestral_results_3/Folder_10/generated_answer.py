def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for string in strings:
        string = string.lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagram_dict:
            anagram_count += 1
            if anagram_count > 21:
                return False
        else:
            anagram_dict[sorted_string] = 1
    return True