def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    length = len(s)
    result = set()
    for i in range(length - 254):
        substring = s[i:i + 255]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result