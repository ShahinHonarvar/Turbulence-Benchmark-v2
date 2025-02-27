def palindromes_of_specific_lengths(s):
    s = s[14:87].lower()
    return {s[i:j + 1] for i in range(len(s) - 50) for j in range(i + 50, len(s) + 1) if s[i:j + 1] == s[i:j + 1][::-1]}