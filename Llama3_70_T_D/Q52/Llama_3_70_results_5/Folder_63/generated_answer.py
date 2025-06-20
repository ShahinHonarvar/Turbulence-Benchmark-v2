def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 17):
        substring = s[i:i + 18]
        if substring.isalpha() and substring == substring[::-1]:
            result.add(substring)
    return result