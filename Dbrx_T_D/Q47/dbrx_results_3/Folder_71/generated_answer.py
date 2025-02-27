def palindromes_of_specific_lengths(s):
    return {s[i:j] for i in range(18, 65) for j in range(i + 23, i + 37) if s[i:j].lower() == s[i:j][::-1].lower() and s[i:j].isalpha()}