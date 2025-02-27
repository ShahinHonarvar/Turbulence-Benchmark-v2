def palindromes_of_specific_lengths(s):
    s = s[18:99]
    return set((p for i in range(18, 99) for j in range(i + 31, min(i + 52, 99)) if p == ''.join((c.lower() for c in s[i:j + 1])) and p[::-1].lower() == ''.join((c.lower() for c in s[i:j + 1]))))