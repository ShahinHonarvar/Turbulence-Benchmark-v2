def if_contains_anagrams(strings):
    string_dict = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) < 3:
            continue
        if sorted_s in string_dict:
            string_dict[sorted_s] += 1
        else:
            string_dict[sorted_s] = 1
    count = 0
    for key in string_dict.keys():
        if count < string_dict[key] // 2:
            count = string_dict[key] // 2
    return count <= 11