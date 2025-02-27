def if_contains_anagrams(str_list):
    seen_anagrams = {}
    for str in str_list:
        str = ''.join(sorted(str.lower()))
        if str in seen_anagrams:
            if seen_anagrams[str] >= 11:
                return False
            else:
                seen_anagrams[str] += 1
        else:
            seen_anagrams[str] = 1
    return True