def palindromes_of_specific_lengths(string):
    substring = string[15:96]
    palindromes = set()
    for length in range(20, 67):
        for start in range(len(substring) - length + 1):
            potential_palindrome = substring[start:start + length]
            if potential_palindrome.isalpha():
                if potential_palindrome.lower() == potential_palindrome[::-1].lower():
                    palindromes.add(potential_palindrome)
    return palindromes