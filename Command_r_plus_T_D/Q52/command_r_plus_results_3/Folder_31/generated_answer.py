def palindrome_of_length_n(s: str) -> set:
    s = s.lower()
    length = len(s)
    result = set()
    for i in range(length):
        for j in range(i + 1, min(i + 67, length + 1)):
            substring = s[i:j]
            if len(substring) == 66 and substring == substring[::-1]:
                result.add(substring)
    return result