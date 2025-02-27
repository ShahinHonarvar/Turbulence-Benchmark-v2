def if_contains_anagrams(str_list):
    seen_anagrams = set()
    for str in str_list:
        str = ''.join(sorted(str.lower())).replace(' ', '')
        if str in seen_anagrams:
            if len(seen_anagrams) >= 70:
                return False
        else:
            seen_anagrams.add(str)
    return True