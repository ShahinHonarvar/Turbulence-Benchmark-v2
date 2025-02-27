def palindrome_of_length_at_least_n(string):
    string = string.lower()
    letters = [c for c in string if c.isalpha()]
    n = len(letters)
    palindromes = set()
    for i in range(18, n + 1):
        for j in range(0, n - i + 1):
            substring = ''.join(letters[j:j + i])
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes