def if_contains_anagrams(strings):
    anagrams_count = 0
    string_set = set()
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3 and sorted_string not in string_set:
            string_set.add(sorted_string)
        elif sorted_string in string_set:
            anagrams_count += 1
            string_set.add(sorted_string)
    return anagrams_count <= 210