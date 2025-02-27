def palindromes_of_specific_lengths(s):
    s = s[33:86].lower()
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 26, i + 32) if s[i:j] == s[i:j][::-1]}
    return {p for p in palindromes if p.isalpha()}