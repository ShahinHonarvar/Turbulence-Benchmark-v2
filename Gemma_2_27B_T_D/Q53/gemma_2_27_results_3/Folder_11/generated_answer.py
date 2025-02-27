def palindrome_of_length_at_least_n(s):
    result = set()
    for i in range(len(s) - 53):
        substring = s[i:i + 54].lower()
        if substring == substring[::-1] and len(substring) >= 54:
            result.add(substring)
    return result