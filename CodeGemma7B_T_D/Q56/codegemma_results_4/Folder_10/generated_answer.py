def all_substring_of_size_n(st):
    len_st = len(st)
    result = []
    for i in range(len_st - 54):
        temp = st[i:i + 55]
        if len(set(temp)) == 55 and temp not in result:
            result.append(temp)
    return result