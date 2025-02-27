def palindrome_of_length_at_least_n(S):
    result = set()
    S = S.lower()
    for i in range(len(S)):
        for j in range(i + 8, len(S)):
            sub = S[i:j + 1]
            if sub == sub[::-1]:
                result.add(sub)
    return result