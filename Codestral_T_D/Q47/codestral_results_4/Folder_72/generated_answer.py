def palindromes_of_specific_lengths(s):
    s = s[26:91]
    s = ''.join(filter(str.isalpha, s)).lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 27, min(i + 59, len(s))) if s[i:j] == s[j - 1:i - 1:-1]}