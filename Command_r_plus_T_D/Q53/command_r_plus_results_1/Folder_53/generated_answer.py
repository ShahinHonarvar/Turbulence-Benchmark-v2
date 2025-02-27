def palindrome_of_length_at_least_n(s: str) -> set:
    s = s.lower()
    result = set()
    for i in range(len(s) - 63):
        for j in range(i + 64, len(s) + 1):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result