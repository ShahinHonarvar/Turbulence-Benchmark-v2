def palindromes_of_specific_lengths(s):
    valid_chars = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    return set((s[i:j + 1] for i in range(33, 86) for j in range(i, min(i + 31, 86)) if len(set(s[i:j + 1]) - set(valid_chars)) == 0 and s[i:j + 1] == s[i:j + 1][::-1]))