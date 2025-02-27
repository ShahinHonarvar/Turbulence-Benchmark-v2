def if_contains_anagrams(str_list):
    str_list = [str.lower() for str in str_list]
    str_list = sorted(str_list, key=len)
    pairs = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]) and len(str_list[i]) >= 3 and (len(str_list[j]) >= 3) and (str_list[i] != str_list[j]):
                pairs += 1
    if pairs <= 19:
        return True
    else:
        return False