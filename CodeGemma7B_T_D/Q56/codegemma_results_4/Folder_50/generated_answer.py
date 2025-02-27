def all_substring_of_size_n(str):
    return [str[i:i + 11] for i in range(len(str) - 10)]