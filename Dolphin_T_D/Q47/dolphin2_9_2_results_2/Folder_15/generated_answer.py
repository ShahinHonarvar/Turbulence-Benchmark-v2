def palindromes_of_specific_lengths(s):
    s = s[:7].lower()
    return {s[i:j + 1] for i in range(len(s)) for j in range(i + 2, len(s) + 1) if s[i:j + 1] == s[i:j + 1][::-1] and 3 <= j - i + 1 <= 6}