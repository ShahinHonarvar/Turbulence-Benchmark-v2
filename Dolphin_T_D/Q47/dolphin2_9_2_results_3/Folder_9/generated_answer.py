def palindromes_of_specific_lengths(string):
    string = string.lower()
    palindromes = set()
    for length in range(50, 61):
        for start in range(301 - length):
            substring = string[start:start + length]
            if substring == substring[::-1]:
                palindrome = ''.join([char for char in substring if char.isalpha()])
                if len(palindrome) in range(50, 61):
                    palindromes.add(palindrome)
    return palindromes