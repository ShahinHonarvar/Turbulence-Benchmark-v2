def palindrome_of_length_at_least_n(string):
    result = set()
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 147:
                result.add(substring.lower())
    return result