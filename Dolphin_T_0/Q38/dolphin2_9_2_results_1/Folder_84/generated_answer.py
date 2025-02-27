def find_subset_of_length_n(S):
    n = 872
    if n > len(S):
        return 0
    S = list(S)
    result = 0
    for i in range(len(S) - n + 1):
        for j in range(i + 1, len(S) - n + 2):
            if len(set(S[i:j + n])) != n:
                result += 1
    return result