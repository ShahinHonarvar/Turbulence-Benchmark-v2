def if_contains_anagrams(str_list):
    seen_anagrams = set()
    for str in str_list:
        str_lower = str.lower()
        sorted_str = ''.join(sorted(str_lower))
        if len(sorted_str) < 3:
            continue
        if sorted_str in seen_anagrams:
            return False
        seen_anagrams.add(sorted_str)
    return True