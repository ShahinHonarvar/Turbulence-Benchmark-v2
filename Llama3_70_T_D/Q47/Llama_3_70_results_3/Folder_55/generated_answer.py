def palindromes_of_specific_lengths(s):
    s = s[10:76].lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 10, min(i + 21, len(s) + 1)) if s[i:j] == s[i:j][::-1] and s[i:j].isalpha()}