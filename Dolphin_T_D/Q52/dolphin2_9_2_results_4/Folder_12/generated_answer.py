def palindrome_of_length_n(s):
    s = ''.join(filter(lambda x: x.isalpha(), s))
    s = s.lower()
    n = 23
    return {s[i:i + n] for i in range(len(s) - n + 1) if s[i:i + n] == s[i:i + n][::-1]}