def palindromes_of_specific_lengths(s):
    s = s[44:100].lower()
    return set(filter(lambda p: 13 <= len(p) <= 42, [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if s[i:j] == s[i:j][::-1]]))