def palindrome_of_length_n(s: str) -> set:
    result = set()
    s = s.lower()
    for i in range(len(s) - 6):
        substring = s[i:i + 7]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result