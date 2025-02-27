def palindrome_of_length_n(s):
    result = set()
    n = 20
    s = s.lower()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result