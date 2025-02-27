def if_contains_anagrams(str_list):
    seen = set()
    pair_count = 0
    for str1 in str_list:
        str1 = str1.lower()
        for str2 in str_list:
            str2 = str2.lower()
            if str1 == str2:
                continue
            sorted_str1 = ''.join(sorted(str1))
            sorted_str2 = ''.join(sorted(str2))
            if sorted_str1 == sorted_str2:
                if str1 not in seen and str2 not in seen:
                    seen.add(str1)
                    seen.add(str2)
                    pair_count += 1
    return pair_count >= 92