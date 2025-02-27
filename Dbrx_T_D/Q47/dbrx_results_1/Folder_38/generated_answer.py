def palindromes_of_specific_lengths(string):
    palindromes = set()
    for length in range(38, 61):
        for start in range(18, 88 - length + 1):
            potential_palindrome = string[start:start + length].lower()
            if potential_palindrome == potential_palindrome[::-1] and potential_palindrome.isalpha():
                palindromes.add(potential_palindrome)
    return palindromes