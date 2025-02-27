def palindromes_of_specific_lengths(s):
    s = s[70:141]
    s = ''.join(filter(str.isalpha, s)).lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 3, min(i + 61, len(s))) if s[i:j] == s[i:j][::-1]}