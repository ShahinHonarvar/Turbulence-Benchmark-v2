def palindrome_of_length_n(string):
    string = string.lower()
    result = set()
    n = 18
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring.isalpha() and substring == substring[::-1]:
            result.add(substring)
    return result