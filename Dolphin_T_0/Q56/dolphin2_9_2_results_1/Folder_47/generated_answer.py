def all_substring_of_size_n(S):
    N = len(S)
    distinct_substrings = []
    for i in range(N - 8):
        substring = S[i:i + 9]
        if len(set(substring)) == 9:
            if substring not in distinct_substrings:
                distinct_substrings.append(substring)
    return distinct_substrings