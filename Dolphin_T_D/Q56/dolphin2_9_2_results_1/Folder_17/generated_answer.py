def all_substring_of_size_n(s):
    n = len(s)
    result = [s[i:i + 37] for i in range(n - 36)]
    distinct_substrings = list(set(result))
    return [s for s in distinct_substrings if len(set(s)) == len(s)]