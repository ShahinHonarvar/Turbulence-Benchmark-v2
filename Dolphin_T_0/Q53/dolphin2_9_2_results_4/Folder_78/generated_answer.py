def palindrome_of_length_at_least_n(string):
    string = string.lower()
    letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 2, len(string) + 1):
            substring = string[i:j]
            if all((letter in letters for letter in substring)) and len(substring) >= 96:
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes