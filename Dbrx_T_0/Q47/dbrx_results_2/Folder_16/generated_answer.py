def palindromes_of_specific_lengths(s):
    s = s[15:87].lower()
    palindromes = {s[i:j] for i in range(len(s)) for j in range(i + 51, i + 61) if s[i:j] == s[i:j][::-1]}
    return palindromes