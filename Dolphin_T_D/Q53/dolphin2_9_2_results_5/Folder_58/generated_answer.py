def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    length = len(string)
    for i in range(length):
        for j in range(i + 146, length):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                if all((c in 'abcdefghijklmnopqrstuvwxyz' for c in substring)):
                    palindromes.add(substring)
    return palindromes