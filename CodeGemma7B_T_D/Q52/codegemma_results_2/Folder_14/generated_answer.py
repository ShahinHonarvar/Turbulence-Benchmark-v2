def palindrome_of_length_n(string):
    palindrome_set = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i + 1, len(string) - 2):
            substring = string[i:j + 3]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set