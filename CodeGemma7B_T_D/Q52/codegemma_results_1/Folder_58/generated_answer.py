def palindrome_of_length_n(string):
    palindrome = set()
    string = string.lower()
    for i in range(len(string) - 222):
        for j in range(i + 1, len(string) - 221):
            for k in range(j + 1, len(string) - 220):
                substring = string[i:k + 1]
                palindrome.add(substring)
    return palindrome