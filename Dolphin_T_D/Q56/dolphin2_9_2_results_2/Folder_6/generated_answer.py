def all_substring_of_size_n(s):
    string_length = len(s)
    min_substring_length = 23
    res = set()
    for i in range(0, string_length - min_substring_length + 1):
        current_substring = s[i:i + min_substring_length]
        if len(set(list(current_substring))) == min_substring_length:
            res.add(current_substring)
    return list(res)