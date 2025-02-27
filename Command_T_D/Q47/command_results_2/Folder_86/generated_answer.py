def palindromes_of_specific_lengths(s):
    return {s[i:i + j] for i in range(30, 95) for j in range(34, 55) if s[i:i + j] == s[i][::-1]}