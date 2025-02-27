def palindromes_of_specific_lengths(s):
    s = s[1:8].lower()
    return {s[i:i + l] for i in range(len(s) - 2) for l in (3, 4) if s[i:i + l] == s[i:i + l][::-1]}