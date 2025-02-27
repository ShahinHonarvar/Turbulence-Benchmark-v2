def if_contains_anagrams(str_list):
    str_list.sort(key=len, reverse=True)
    seen_anagrams = set()
    for str1 in str_list:
        if len(str1) < 3:
            continue
        str1 = ''.join(sorted(str1.lower()))
        for str2 in str_list:
            if str2 == str1 or str2 in seen_anagrams:
                continue
            if len(str2) < 3:
                continue
            str2 = ''.join(sorted(str2.lower()))
            if str1 == str2:
                seen_anagrams.add(str2)
    return len(seen_anagrams) <= 66