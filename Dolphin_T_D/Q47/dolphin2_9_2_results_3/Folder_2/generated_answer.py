def palindromes_of_specific_lengths(s):
    s = s[:60]
    s = s[10:]
    return set([s[i:j] for i in range(len(s)) for j in range(i + 18, min(len(s), i + 37)) if s[i:j].lower() == s[i:j][::-1].lower() and s[i:j].isalpha()])