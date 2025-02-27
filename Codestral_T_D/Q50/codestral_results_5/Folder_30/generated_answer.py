def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string] += 1
                anagram_count += anagram_dict[sorted_string] - 1
            else:
                anagram_dict[sorted_string] = 1
    return anagram_count >= 78