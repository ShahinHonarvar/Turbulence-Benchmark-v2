def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    length = len(s)
    result = set()
    for i in range(length - 40):
        substring = s[i:i + 41]
        if substring == substring[::-1]:
            result.add(substring)
    return result