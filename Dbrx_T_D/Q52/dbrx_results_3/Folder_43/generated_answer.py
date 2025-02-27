def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = 51
    if n <= 0 or (n % 2 == 1 and n > len(s)) or (n % 2 == 0 and n / 2 > len(s)):
        return set()
    result = set()
    for i in range(len(s) - n + 1):
        if s[i:i + n] == s[i:i + n][::-1]:
            result.add(s[i:i + n])
    return result