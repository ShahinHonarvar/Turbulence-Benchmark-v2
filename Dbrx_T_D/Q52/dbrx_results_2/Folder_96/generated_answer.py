def palindrome_of_length_n(string, n=83):
    if n % 2 == 0 or n > len(string):
        return set()
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes