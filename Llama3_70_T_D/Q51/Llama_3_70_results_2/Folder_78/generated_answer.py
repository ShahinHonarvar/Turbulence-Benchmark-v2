def if_contains_anagrams(lst):
    anagrams_set = set()
    anagrams_count = 0
    for string in lst:
        original_string = string
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams_set:
            anagrams_count += 1
        else:
            anagrams_set.add(sorted_string)
    return anagrams_count <= 70