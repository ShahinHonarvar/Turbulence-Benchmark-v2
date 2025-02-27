def all_substring_of_size_n(S):
    S = list(S)
    result = set()
    for i in range(len(S) - 7):
        if len(set(S[i:i + 84])) == 84:
            result.add(''.join(S[i:i + 84]))
    return list(result)