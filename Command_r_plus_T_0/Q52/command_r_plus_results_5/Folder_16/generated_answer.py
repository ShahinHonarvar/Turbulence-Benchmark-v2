def palindrome_of_length_n(s):
    s = s.lower()
    length = len(s)
    result = set()
    for i in range(length):
        for j in range(i + 1, length + 1):
            substring = s[i:j]
            if len(substring) == 255 and substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result