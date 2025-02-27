def if_contains_anagrams(lst):
    anagrams_dict = {}
    anagrams_count = 0
    for string in lst:
        lower_case_string = string.lower()
        filtered_string = ''.join(filter(str.isalpha, lower_case_string))
        if len(filtered_string) < 3:
            continue
        sorted_string = ''.join(sorted(filtered_string))
        anagrams_dict[sorted_string] = anagrams_dict.get(sorted_string, 0) + 1
    for key in anagrams_dict:
        n = anagrams_dict[key]
        anagrams_count += n * (n - 1) // 2
    return anagrams_count <= 206