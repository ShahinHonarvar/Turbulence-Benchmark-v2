def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1]:
                result.add(substring.lower())
    return result