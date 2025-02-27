def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s) - 6):
        for j in range(i + 7, len(s) + 1):
            substring = s[i:j].lower()
            if substring == substring[::-1]:
                result.add(substring)
    return result