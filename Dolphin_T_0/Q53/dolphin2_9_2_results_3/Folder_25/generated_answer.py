def palindrome_of_length_at_least_n(s):
    result = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 38, length):
            substring = s[i:j + 1].lower()
            if substring == substring[::-1]:
                result.add(substring)
    return result