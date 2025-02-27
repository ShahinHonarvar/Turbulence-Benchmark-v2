def if_contains_anagrams(str_list):
    seen_anagrams = set()
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in seen_anagrams:
            return False
        seen_anagrams.add(sorted_string)
    return True