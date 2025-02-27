def if_contains_anagrams(list_of_strings):
    seen_anagrams = set()
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3 and sorted_string not in seen_anagrams:
            seen_anagrams.add(sorted_string)
    return len(seen_anagrams) <= 60