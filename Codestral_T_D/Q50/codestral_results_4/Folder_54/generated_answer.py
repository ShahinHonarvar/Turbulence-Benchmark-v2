def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            if sorted_string in anagram_dict:
                anagram_dict[sorted_string].append(lower_string)
            else:
                anagram_dict[sorted_string] = [lower_string]
            if len(anagram_dict[sorted_string]) >= 2:
                anagram_count += 1
    return anagram_count >= 74