import re

def palindromes_of_specific_lengths(str):
    """
    This function takes a string as input and returns the set of all palindromes with the following requirements.
    - Only palindromes occurring in the substring from index 23 to index 77, both inclusive, should be considered.
    - Only palindromes of lengths between 13 to 40 (both inclusive) should be considered.
    - Each palindrome should only consist of English letters.
    - If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    - The function should find the palindromes in a case-insensitive manner.
    """
    palindrome_pattern = re.compile('^[a-zA-Z]{13,40}$')
    valid_palindromes = set()
    for i in range(23, 78):
        substring = str[i:i + 14]
        if palindrome_pattern.match(substring):
            valid_palindromes.add(substring.lower())
        substring = str[i:i - 14:-1]
        if palindrome_pattern.match(substring):
            valid_palindromes.add(substring.lower())
    return valid_palindromes