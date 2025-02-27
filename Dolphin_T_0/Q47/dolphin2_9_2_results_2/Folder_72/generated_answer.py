def palindromes_of_specific_lengths(s):
    return set((s[i:i + k] for i in range(26, 91 - k + 1) for k in range(27, 59) if s[i:i + k].lower() == s[i:i + k][::-1].lower()))