def if_contains_anagrams(lst):
    anagrams_count = 0
    anagrams_dict = {}
    for string in lst:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams_dict:
            anagrams_count += len(anagrams_dict[sorted_string])
            anagrams_dict[sorted_string].add(string)
        else:
            anagrams_dict[sorted_string] = {string}
    return anagrams_count <= 18