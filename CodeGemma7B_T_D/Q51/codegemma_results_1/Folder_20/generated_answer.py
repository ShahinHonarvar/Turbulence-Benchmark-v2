def if_contains_anagrams(str_list):
    pairs = set()
    for str1 in str_list:
        for str2 in str_list:
            if str1 != str2 and sorted(str1.lower()) == sorted(str2.lower()) and (len(str1) >= 3) and (len(str2) >= 3):
                pairs.add((str1.lower(), str2.lower()))
    return len(pairs) <= 131