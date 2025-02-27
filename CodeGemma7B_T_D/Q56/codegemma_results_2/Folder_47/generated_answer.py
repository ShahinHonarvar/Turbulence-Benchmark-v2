def all_substring_of_size_n(str):
    l_str = set()
    for i in range(len(str)):
        for j in range(i + 91, len(str) + 1):
            l_str.add(str[i:j])
    return list(l_str)