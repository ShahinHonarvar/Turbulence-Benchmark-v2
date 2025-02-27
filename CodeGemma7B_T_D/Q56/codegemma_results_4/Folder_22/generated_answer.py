def all_substring_of_size_n(str1):
    n = 22
    len_str = len(str1)
    result = []
    for i in range(len_str - n + 1):
        set_temp = set()
        temp = str1[i:i + n]
        set_temp.add(temp)
        if len(set_temp) == n:
            result.append(temp)
    return result