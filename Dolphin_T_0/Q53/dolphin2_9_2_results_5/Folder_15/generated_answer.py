def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for length in range(4, len(string) + 1):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if ''.join(reversed(substring)) == substring:
                palindromes.add(substring)
    return palindromes