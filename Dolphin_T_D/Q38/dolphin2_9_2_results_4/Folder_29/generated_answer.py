def find_subset_of_length_n(S):
    if len(S) < 19:
        return 0
    result = 0
    for i in range(len(S) - 19):
        result += S.count(i)
    return result