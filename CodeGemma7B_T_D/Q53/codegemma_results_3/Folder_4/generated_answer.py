def palindrome_of_length_at_least_n(str):
    result = set()
    str = str.lower()
    for i in range(len(str)):
        for j in range(i + 2, len(str) + 1):
            substring = str[i:j]
            if substring == substring[::-1] and len(substring) >= 99:
                result.add(substring)
    return result