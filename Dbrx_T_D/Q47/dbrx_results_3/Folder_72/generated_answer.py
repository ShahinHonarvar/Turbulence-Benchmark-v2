def palindromes_of_specific_lengths(s):
    s = s[26:91].lower()
    palindromes = {s[i:j] for length in range(27, 59) for i in range(len(s) - length + 1) for j in range(i + 1, i + length + 1) if s[i:j] == s[i:j][::-1]}
    return palindromes