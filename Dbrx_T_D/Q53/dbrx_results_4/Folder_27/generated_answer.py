def palindrome_of_length_at_least_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    return {palindrome for i in range(len(s)) for j in range(i, i + 100) if j < len(s) for palindrome in {s[i:j + 1], s[i:j + 1][::-1]} if palindrome == palindrome[::-1] and len(palindrome) >= 100}