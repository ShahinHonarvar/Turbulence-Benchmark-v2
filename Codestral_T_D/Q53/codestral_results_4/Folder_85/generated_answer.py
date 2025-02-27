def palindrome_of_length_at_least_n(string):
    palindromes = set()
    n = 85
    for i in range(len(string)):
        for j in range(i + n, len(string) + 1):
            substring = string[i:j]
            if substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes