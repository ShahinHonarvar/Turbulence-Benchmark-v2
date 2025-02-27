def palindromes_of_specific_lengths(s):
    s = s[:21].lower()
    return {s[i:j + 1] for i in range(len(s)) for j in range(i + 4, min(i + 81, len(s))) if s[i:j + 1] == s[i:j + 1][::-1] and s[i:j + 1].isalpha()}