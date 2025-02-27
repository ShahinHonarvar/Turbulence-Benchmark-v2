def all_substring_of_size_n(str1):
    if len(str1) < 75:
        return []
    return list(map(set, [str1[i:i + 75] for i in range(len(str1) - 74)]))