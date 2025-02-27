def palindromes_of_specific_lengths(s):
    s = s[40:95].lower()
    return {s[i:i + l] for l in range(45, 52) for i in range(len(s) - l + 1) if s[i:i + l] == s[i:i + l][::-1]}