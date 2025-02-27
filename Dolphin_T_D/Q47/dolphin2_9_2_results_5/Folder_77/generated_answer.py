def palindromes_of_specific_lengths(s):
    s = s[103:277]
    return {s[i:i + l] for l in range(100, 170) for i in range(len(s) - l + 1) if all((c.isalpha() for c in s[i:i + l])) and s[i:i + l].lower() == s[i:i + l][::-1].lower()}