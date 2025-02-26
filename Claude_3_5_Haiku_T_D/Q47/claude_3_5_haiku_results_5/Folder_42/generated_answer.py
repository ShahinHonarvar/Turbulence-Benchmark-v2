def palindromes_of_specific_lengths(text):
    if len(text) < 96:
        return set()
    substring = text[43:96].lower()
    valid_palindromes = set()
    for length in range(18, 48):
        for start in range(len(substring) - length + 1):
            potential_palindrome = substring[start:start + length]
            if all((char.isalpha() for char in potential_palindrome)):
                if potential_palindrome == potential_palindrome[::-1]:
                    valid_palindromes.add(potential_palindrome)
    return valid_palindromes