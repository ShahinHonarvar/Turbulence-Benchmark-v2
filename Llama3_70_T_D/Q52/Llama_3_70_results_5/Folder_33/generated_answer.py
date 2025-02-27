def palindrome_of_length_n(string):
    n = 475
    string = string.lower()
    palindrome_set = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring.isalpha() and substring == substring[::-1]:
            palindrome_set.add(substring)
    return palindrome_set