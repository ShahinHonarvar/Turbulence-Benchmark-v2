def palindrome_of_length_at_least_n(string):
    result = set()
    string = ''.join((c.lower() for c in string if c.isalpha()))
    n = len(string)
    for i in range(n):
        for j in range(i + 76, n + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result