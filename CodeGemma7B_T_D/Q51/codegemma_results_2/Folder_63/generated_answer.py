def if_contains_anagrams(str_list):
    anagrams = set()
    for str in str_list:
        sorted_str = ''.join(sorted(str.lower()))
        if len(sorted_str) >= 3 and sorted_str in anagrams:
            return False
        anagrams.add(sorted_str)
    return True