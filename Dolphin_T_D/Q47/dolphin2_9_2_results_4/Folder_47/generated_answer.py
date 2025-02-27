def palindromes_of_specific_lengths(s):
    substring = s[39:95]
    palindromes = set()
    for length in range(14, 53):
        for i in range(len(substring) - length + 1):
            potential_palindrome = substring[i:i + length]
            if all((char.isalpha() for char in potential_palindrome)):
                potential_palindrome = potential_palindrome.lower()
                if potential_palindrome == ''.join(reversed(potential_palindrome)):
                    palindromes.add(potential_palindrome)
    return palindromes