def all_substring_of_size_n(S):
    if len(set(S)) < 52:
        return []
    subs = {S[i:i + 52] for i in range(len(S) - 51)}
    return list(subs)