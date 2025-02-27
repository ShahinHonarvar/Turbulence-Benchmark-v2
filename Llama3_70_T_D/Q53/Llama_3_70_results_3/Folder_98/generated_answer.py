def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    length = len(s)
    for i in range(length):
        for j in range(i + 6, length + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result