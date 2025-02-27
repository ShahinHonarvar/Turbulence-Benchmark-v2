def palindromes_of_specific_lengths(text):
    substring = text[63:71].lower()
    palindromes = set()
    for i in range(len(substring) - 3):
        for j in range(i + 4, min(i + 6, len(substring)) + 1):
            potential_palindrome = substring[i:j]
            if potential_palindrome == potential_palindrome[::-1] and all((c.isalpha() for c in potential_palindrome)):
                palindromes.add(potential_palindrome)
    return palindromes