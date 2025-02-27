def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 186 + 1):
        substring = s[i:i + 186]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result