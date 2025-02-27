def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[:51]
    for length in range(50, 101):
        for start in range(len(substring) - length + 1):
            palindrome = substring[start:start + length]
            if palindrome.isalpha():
                if palindrome.lower() == palindrome.lower()[::-1]:
                    palindromes.add(palindrome)
    return palindromes