def palindrome_of_length_n(s):
    s = s.lower()
    result = set()
    palindrome = ''
    for length in range(94, 0, -1):
        for i in range(len(s)):
            if i + length <= len(s):
                substring = s[i:i + length]
                if substring == substring[::-1] and substring.isalpha():
                    result.add(substring)
    return result