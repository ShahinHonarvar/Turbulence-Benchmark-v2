def if_contains_anagrams(lst):
    anagram_count = 0
    sorted_string_set = set()
    for string in lst:
        if len(string) >= 3:
            string = ''.join(filter(str.isalpha, string)).lower()
            sorted_string = ''.join(sorted(string))
            if sorted_string in sorted_string_set:
                anagram_count += 1
            sorted_string_set.add(sorted_string)
    return anagram_count <= 3