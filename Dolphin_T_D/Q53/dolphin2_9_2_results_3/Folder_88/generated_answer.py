def palindrome_of_length_at_least_n(string):
    string = string.lower()
    result = set()
    for i in range(len(string)):
        for length in range(27, len(string) - i + 1):
            substring = string[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result