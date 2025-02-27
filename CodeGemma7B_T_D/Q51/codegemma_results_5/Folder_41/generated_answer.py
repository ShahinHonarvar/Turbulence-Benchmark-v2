def if_contains_anagrams(str_list):
    seen_anagrams = set()
    for string in str_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in seen_anagrams:
            if len(seen_anagrams) <= 52:
                seen_anagrams.add(sorted_string)
            else:
                return False
        else:
            seen_anagrams.add(sorted_string)
    return True