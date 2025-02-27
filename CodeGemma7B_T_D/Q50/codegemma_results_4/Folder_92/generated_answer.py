def if_contains_anagrams(str_list):
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) != len(str_list[j]):
                continue
            str1 = ''.join(sorted([c for c in str_list[i] if c.isalpha()]))
            str2 = ''.join(sorted([c for c in str_list[j] if c.isalpha()]))
            if str1 == str2:
                return True
    return False