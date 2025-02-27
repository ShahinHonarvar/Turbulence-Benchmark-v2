def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string] += 1
                anagram_count += anagram_dict[sorted_string] - 1
                if anagram_count >= 11:
                    return True
            else:
                anagram_dict[sorted_string] = 1
    return anagram_count >= 11