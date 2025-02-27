def if_contains_anagrams(str_list):
    str_list = [i.lower() for i in str_list if len(i) >= 3]
    ans_dict = {}
    for word in str_list:
        key = ''.join(sorted(word))
        if key in ans_dict:
            ans_dict[key] += 1
        else:
            ans_dict[key] = 1
    count = 0
    for items in ans_dict.values():
        if items > 1:
            count += items * (items - 1) // 2
    return count >= 75