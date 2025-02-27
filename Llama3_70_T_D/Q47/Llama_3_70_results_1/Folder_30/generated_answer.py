def palindromes_of_specific_lengths(s):
    s = s[14:91].lower()
    return set((sub for i in range(len(s)) for sub in (s[i:i + j] for j in range(55, 72) if s[i:i + j] == s[i:i + j][::-1] and sub.isalpha())))