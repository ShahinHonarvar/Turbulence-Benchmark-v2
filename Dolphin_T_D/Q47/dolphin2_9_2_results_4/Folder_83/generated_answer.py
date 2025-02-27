from string import ascii_letters

def palindromes_of_specific_lengths(s):
    s = ''.join((c.lower() for c in s[75:96] if c in ascii_letters))
    return {s[i:j] for i in range(len(s) - 7) for j in range(i + 7, min(i + 10, len(s) + 1)) if s[i:j] == s[i:j][::-1]}