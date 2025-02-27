def all_substring_of_size_n(S):
    n = len(S)
    answer = set()
    for i in range(n):
        for j in range(i + 38, n):
            if len(set(S[i:j])) == 38:
                answer.add(S[i:j])
    return list(answer)