def palindrome_of_length_at_least_n(s):
    s = ''.join((e.lower() for e in s if e.isalpha()))
    return {sub for i in range(len(s) - 18) for j in range(i, len(s) - 18 + i) if (sub := s[i:j + i + 1]) == sub[::-1] and len(sub) >= 19}