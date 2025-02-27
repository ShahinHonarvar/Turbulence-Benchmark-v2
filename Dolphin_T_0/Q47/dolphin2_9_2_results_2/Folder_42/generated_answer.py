def palindromes_of_specific_lengths(s):
    substring = s[43:96].lower()
    return {s[i:j] for i in range(len(substring)) for j in range(i + 18, len(substring) + 1) if s[i:j] == s[i:j][::-1] and s[i:j].isalpha()}