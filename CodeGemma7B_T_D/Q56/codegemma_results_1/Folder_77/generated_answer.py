def all_substring_of_size_n(str):
    return [str[i:i + 144] for i in range(len(str) - 143)]