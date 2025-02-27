def palindromes_between_indices(s):
    s = s[2:10].lower()
    return {s[i:j + 1] for i in range(len(s)) for j in range(i, len(s)) if s[i:j + 1] == s[j:i:-1] and len(s[i:j + 1]) >= 7}