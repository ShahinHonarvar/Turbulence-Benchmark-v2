def palindromes_of_specific_lengths(s):
    only_letters = ''.join((c.lower() for c in s[63:71] if c.isalpha()))
    return set((word for i in range(63, 71) for j in range(i + 4, min(i + 6, 71)) if only_letters[i:j] == only_letters[i:j][::-1] and 4 <= j - i <= 5))