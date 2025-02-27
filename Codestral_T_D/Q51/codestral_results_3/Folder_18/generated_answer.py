def if_contains_anagrams(strings):
    count = 0
    anagram_dict = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string] += 1
                count += anagram_dict[sorted_string]
            else:
                anagram_dict[sorted_string] = 0
    return count <= 42