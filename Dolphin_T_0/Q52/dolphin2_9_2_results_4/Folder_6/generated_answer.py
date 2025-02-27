def palindrome_of_length_n():
    n = 474
    string = 'string'
    substrings = set()
    for i in range(len(string)):
        for j in range(i + n, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                substrings.add(substring.lower())
    return substrings