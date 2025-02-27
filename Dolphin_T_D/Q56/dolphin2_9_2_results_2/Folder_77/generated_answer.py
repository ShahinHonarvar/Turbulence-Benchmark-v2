def all_substring_of_size_n(input_str):
    res = []
    for i in range(len(input_str)):
        for j in range(i + 144, len(input_str) + 1):
            if len(set(input_str[i:j])) == 144:
                res.append(input_str[i:j])
    return list(set(res))