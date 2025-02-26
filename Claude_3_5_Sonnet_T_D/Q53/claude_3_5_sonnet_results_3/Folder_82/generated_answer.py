def palindrome_of_length_at_least_n(string):
    result = set()
    string = ''.join((char.lower() for char in string if char.isalpha()))
    length = len(string)
    for i in range(length):
        for j in range(i + 72, length + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result