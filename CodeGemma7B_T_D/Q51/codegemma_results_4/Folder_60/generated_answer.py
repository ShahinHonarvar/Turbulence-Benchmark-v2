def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    pairs = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str1 = ''.join(sorted(str_list[i]))
            str2 = ''.join(sorted(str_list[j]))
            if str1 == str2 and len(str1) >= 3:
                pairs += 1
    return pairs <= 77