def palindrome_of_length_at_least_n(string):
    result = set()
    string = ''.join((char.lower() for char in string if char.isalpha()))
    n = len(string)
    for i in range(n):
        for j in range(i + 97, n + 1):
            substring = string[i:j]
            if substring == substring[::-1] and len(substring) >= 97:
                result.add(substring)
    return result