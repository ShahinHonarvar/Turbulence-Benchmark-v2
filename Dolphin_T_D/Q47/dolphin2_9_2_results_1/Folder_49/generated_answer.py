def palindromes_of_specific_lengths(s):
    s = s[9:101].lower()
    return {s[i:j] for i in range(len(s) - 9) for j in range(i + 10, len(s) + 1) if s[i:j] == s[i:j][::-1] and all((c.isalpha() for c in s[i:j]))}