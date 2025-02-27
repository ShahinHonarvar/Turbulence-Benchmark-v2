def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s) - 36):
        for j in range(i + 37, len(s) + 1):
            substring = s[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result