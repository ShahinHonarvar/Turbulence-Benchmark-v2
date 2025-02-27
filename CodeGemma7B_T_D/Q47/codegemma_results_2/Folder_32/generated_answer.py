import re

def palindromes_of_specific_lengths(string):
    """Only palindromes occurring in the substring from index 16 to index 77, both inclusive, should be considered.
   Only palindromes of lengths between 43 to 47 (both inclusive) should be considered.
   Each palindrome should only consist of English letters. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
   The function should find the palindromes in a case-insensitive manner."""
    text = string[16:77]
    pattern = re.compile('(?i)([a-zA-Z]{43,47})')
    found_palindromes = set()
    for match in pattern.finditer(text):
        palindrome = match.group(0)
        if palindrome.lower() in found_palindromes:
            continue
        found_palindromes.add(palindrome)
    return found_palindromes