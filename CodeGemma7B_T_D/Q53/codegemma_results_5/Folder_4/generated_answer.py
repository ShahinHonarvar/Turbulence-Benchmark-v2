from re import finditer

def palindrome_of_length_at_least_n(string):
    """
    This function finds all palindromes of length greater than or equal to 99 in a given string.
    """
    string = string.lower()
    palindromes = set()
    for match in finditer('(?i)[a-z]{99,}', string):
        palindrome = match.group(0)
        palindromes.add(palindrome)
    return palindromes