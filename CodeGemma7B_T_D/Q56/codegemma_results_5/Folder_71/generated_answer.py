def all_substring_of_size_n(str_var):
    res = set()
    for i in range(len(str_var)):
        for j in range(i + 17, len(str_var) + 1):
            res.add(str_var[i:j])
    return list(res)