def palindrome_of_length_at_least_n(string):
    string = string.lower()
    length = len(string)
    palindromes = set()
    for i in range(length):
        for j in range(i + 9, length + 1):
            substring = string[i:j]
            if all((c in 'abcdefghijklmnopqrstuvwxyz' for c in substring)):
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes