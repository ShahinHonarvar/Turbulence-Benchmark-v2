def palindrome_of_length_at_least_n(string):
    string = ''.join((char.lower() for char in string if char.isalpha()))
    result = set()
    n = len(string)
    for i in range(n):
        for j in range(i + 35, n + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result