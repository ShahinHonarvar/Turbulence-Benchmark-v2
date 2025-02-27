def if_contains_anagrams(strings_list):
    anagrams_count = 0
    strings_set = set()
    for string in strings_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in strings_set:
                anagrams_count += 1
            else:
                strings_set.add(sorted_string)
    return anagrams_count >= 29