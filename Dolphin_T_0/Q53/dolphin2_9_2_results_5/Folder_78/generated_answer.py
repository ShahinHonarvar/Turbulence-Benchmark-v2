def palindrome_of_length_at_least_n(string):
    string = string.lower()
    letter_set = set('abcdefghijklmnopqrstuvwxyz')
    palindrome_set = set()
    for length in range(96, len(string) + 1):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if all((char in letter_set for char in substring)):
                if substring == substring[::-1]:
                    palindrome_set.add(substring)
    return palindrome_set