def palindrome_of_length_n(strings):
    result = set()
    for string in strings:
        for i in range(len(string) - 17 + 1):
            substring = string[i:i + 17]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                result.add(substring)
    return result