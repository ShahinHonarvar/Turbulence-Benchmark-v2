def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for length in range(57, len(string) + 1):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
    return palindromes