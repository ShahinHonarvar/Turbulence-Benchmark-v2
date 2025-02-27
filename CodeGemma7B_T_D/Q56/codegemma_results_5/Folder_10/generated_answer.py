def all_substring_of_size_n(str):
    if len(str) >= 55:
        return [str[i:i + 55] for i in range(len(str) - 54)]
    return []