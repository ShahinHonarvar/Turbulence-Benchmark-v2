def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j].lower()
            if substring == substring[::-1] and len(substring) == 46:
                result.add(substring)
    return result