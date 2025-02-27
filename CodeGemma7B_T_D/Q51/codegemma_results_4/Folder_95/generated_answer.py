def if_contains_anagrams(str_list):
    seen_anagrams = set()
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower().replace(' ', '')))
        if sorted_string in seen_anagrams:
            return True
        seen_anagrams.add(sorted_string)
    return False