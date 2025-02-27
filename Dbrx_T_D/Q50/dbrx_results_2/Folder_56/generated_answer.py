def if_contains_anagrams(strings_list):
    anagrams_count = 0
    anagrams_sets = set()
    for string in strings_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagrams_sets:
                anagrams_count += 1
            else:
                anagrams_sets.add(sorted_string)
    return anagrams_count >= 77