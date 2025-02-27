def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    length = len(s)
    result = set()
    for i in range(length):
        for j in range(i + 96, length + 1):
            substring = s[i:j]
            if substring == substring[::-1] and all((char.isalpha() for char in substring)):
                result.add(substring)
    return result