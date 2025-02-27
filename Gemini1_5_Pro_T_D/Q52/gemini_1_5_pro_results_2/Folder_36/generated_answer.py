def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 337):
        substring = s[i:i + 338].lower()
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result