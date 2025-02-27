def palindromes_of_specific_lengths(s):
    s = s[12:57].lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 20, i + 22) if s[i:j] == s[i:j][::-1] and s[i:j].isalpha()}