def all_substring_of_size_n(string):
    return [substring for i in range(len(string) - 38) for substring in [string[i:i + 39]] if len(set(substring)) == 39]