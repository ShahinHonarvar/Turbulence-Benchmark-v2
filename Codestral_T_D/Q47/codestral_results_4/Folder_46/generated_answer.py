def palindromes_of_specific_lengths(s):
    s = s[11:98].lower()
    return {s[i:i + l] for i in range(len(s) - 61) for l in range(29, 63) if s[i:i + l] == s[i:i + l][::-1] and s[i:i + l].isalpha()}