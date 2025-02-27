def palindromes_of_specific_lengths(s):
    s = s[18:88].lower()
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 38, i + 61) if s[i:j] == s[i:j][::-1]}
    return palindromes