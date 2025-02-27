def if_contains_anagrams(strings):
    anagrams_dict = {}
    anagram_pairs = 0
    for string in strings:
        string = ''.join(filter(str.isalpha, string)).lower()
        sorted_string = ''.join(sorted(string))
        if len(string) < 3:
            continue
        if sorted_string in anagrams_dict:
            anagrams_dict[sorted_string] += 1
        else:
            anagrams_dict[sorted_string] = 1
    for count in anagrams_dict.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 36