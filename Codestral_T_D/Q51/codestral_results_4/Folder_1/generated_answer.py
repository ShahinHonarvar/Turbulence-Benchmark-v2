def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_dict = {}
    for string in strings:
        string = string.lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string].append(string)
            anagram_count += len(anagram_dict[sorted_string]) - 1
        else:
            anagram_dict[sorted_string] = [string]
    return anagram_count <= 30