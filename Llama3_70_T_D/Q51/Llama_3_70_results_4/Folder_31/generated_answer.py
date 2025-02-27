def if_contains_anagrams(list_of_strings):
    anagram_count = {}
    for string in list_of_strings:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagram_count:
            anagram_count[sorted_string] += 1
        else:
            anagram_count[sorted_string] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return anagram_pairs <= 65