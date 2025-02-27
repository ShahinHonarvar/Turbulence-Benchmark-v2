def if_contains_anagrams(str_list):
    str_set = set([s.lower() for s in str_list if len(s) >= 3])
    pairs = 0
    for str1 in str_set:
        for str2 in str_set:
            if str1 != str2 and sorted(str1) == sorted(str2):
                pairs += 1
    return pairs >= 3