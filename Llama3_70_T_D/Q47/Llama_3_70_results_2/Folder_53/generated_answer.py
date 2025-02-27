def palindromes_of_specific_lengths(s):
    s = s[1:300].lower()
    return {s[i:j] for j in range(len(s), 2, -1) for i in range(j) if s[i:j] == s[i:j][::-1] and s[i:j].isalpha() and (3 <= len(s[i:j]) <= 10)}