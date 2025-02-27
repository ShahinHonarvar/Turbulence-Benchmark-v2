def palindrome_of_length_n(s):
    s = s.lower()
    n = 74
    result = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if all((char.isalpha() for char in substring)) and substring == substring[::-1]:
            result.add(substring)
    return result