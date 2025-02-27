def palindromes_of_specific_lengths(s):
    s = s[22:96].lower()
    return set((i for i in range(len(s)) for j in range(i + 52, min(i + 56, len(s) + 1)) if set(s[i:j]).issubset('abcdefghijklmnopqrstuvwxyz') and s[i:j] == s[i:j][::-1]))