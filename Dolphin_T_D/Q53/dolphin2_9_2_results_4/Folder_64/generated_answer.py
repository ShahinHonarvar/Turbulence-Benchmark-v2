def palindrome_of_length_at_least_n(string):
    string = string.lower()
    string = ''.join((c for c in string if c.isalpha()))
    n = 9
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes