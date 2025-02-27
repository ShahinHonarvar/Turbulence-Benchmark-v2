def palindrome_of_length_at_least_n(S):
    S = S.lower()
    result = set()
    for i in range(len(S)):
        for j in range(i + 76, len(S) + 1):
            if len(set(S[i:j])) <= 2:
                result.add(S[i:j])
    return result