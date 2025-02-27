def palindrome_of_length_n(s):
    result = set()
    s = s.lower()
    for i in range(len(s) - 72):
        substring = s[i:i + 73]
        if all((c.isalpha() for c in substring)):
            if substring == substring[::-1]:
                result.add(substring)
    return result