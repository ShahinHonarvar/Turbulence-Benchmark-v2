def palindrome_of_length_at_least_n(string):
    string = string.lower()
    result = set()
    for length in range(56, len(string) + 1):
        for i in range(0, len(string) - length + 1):
            substring = string[i:i + length]
            if len(substring) != len(set(substring)):
                continue
            if substring == substring[::-1]:
                result.add(substring)
    return result