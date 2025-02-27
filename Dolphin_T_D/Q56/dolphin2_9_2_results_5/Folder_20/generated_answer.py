def all_substring_of_size_n(string):
    n = 50
    substrings = [string[i:i + n] for i in range(len(string) - n + 1)]
    distinct_substrings = [substring for substring in substrings if len(set(substring)) == n]
    return distinct_substrings