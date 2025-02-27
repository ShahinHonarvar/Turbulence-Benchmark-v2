def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams.append(sorted_string)
    anagrams_count = len(list(filter(lambda x: anagrams.count(x) >= 2, anagrams)))
    return anagrams_count >= 40