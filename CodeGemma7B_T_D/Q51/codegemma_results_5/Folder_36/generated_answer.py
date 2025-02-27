def if_contains_anagrams(str_list):
    anagrams = set()
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower(), key=str.lower))
        if len(sorted_string) >= 3 and sorted_string not in anagrams:
            anagrams.add(sorted_string)
    return len(anagrams) <= 25