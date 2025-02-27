import re

def palindromes_of_specific_lengths(text):
    substring = text[75:96]
    palindromes = set()
    for i in range(len(substring) - 6):
        for length in range(7, 10):
            if i + length <= len(substring):
                potential_palindrome = substring[i:i + length]
                if re.match('^[a-zA-Z]+$', potential_palindrome) and potential_palindrome.lower() == potential_palindrome[::-1].lower():
                    palindromes.add(potential_palindrome)
    return palindromes