def if_contains_anagrams(str_list):
    pairs = set()
    for str1 in str_list:
        str1 = ''.join(sorted(str1.lower()))
        for str2 in str_list:
            if str1 != str2 and str1 in pairs:
                return False
            elif str1 != str2 and str2 not in pairs and (len(str1) >= 3) and (len(str2) >= 3) and (str1 + str2 not in pairs):
                pairs.add(str1 + str2)
    return True