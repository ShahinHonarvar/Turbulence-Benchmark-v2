def if_contains_anagrams(strings_list):
    anagrams_count = 0
    anagrams_set = set()
    for string in strings_list:
        string = string.lower()
        sorted_string = ''.join(sorted(string))
        if len(sorted_string) >= 3 and sorted_string not in anagrams_set:
            anagrams_set.add(sorted_string)
            anagrams_count += 1
    return anagrams_count <= 40