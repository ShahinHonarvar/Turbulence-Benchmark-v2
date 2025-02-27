def palindrome_of_length_n(string, n=24):
    palindrome_set = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n].lower()
        if substring == substring[::-1]:
            palindrome_set.add(substring)
    return palindrome_set