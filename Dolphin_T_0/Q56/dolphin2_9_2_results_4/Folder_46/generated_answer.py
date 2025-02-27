def all_substring_of_size_n(S):
    n = 87
    substring_list = [S[i:i + n] for i in range(len(S) - n + 1)]
    return [substring for substring in substring_list if len(set(substring)) == n]