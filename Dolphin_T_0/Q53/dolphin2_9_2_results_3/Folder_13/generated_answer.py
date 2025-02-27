def palindrome_of_length_at_least_n(string):
    n = 52
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + n, len(string) + 1):
            substring = string[i:j].lower()
            if substring == substring[::-1] and len(substring) >= n:
                palindromes.add(substring)
    return palindromes