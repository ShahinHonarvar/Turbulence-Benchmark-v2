def palindrome_of_length_at_least_n(string):
    string = string.lower()
    string = ''.join((c for c in string if c.isalpha()))
    result = set()
    for i in range(len(string) - 65):
        for j in range(i + 66, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result