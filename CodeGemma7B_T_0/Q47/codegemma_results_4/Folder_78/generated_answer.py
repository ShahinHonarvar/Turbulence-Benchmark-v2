import re

def palindromes_of_specific_lengths(text):
    """
    This function takes a string and returns the set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 15 to index 72, both inclusive, should be considered.
    Only palindromes of lengths between 19 to 55 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    text = text.lower()
    pattern = re.compile('(?<=[\\\\s\\\\w]{15})([a-z]{19,55})[\\\\s\\\\w]{15,57}(?=[\\\\s\\\\w]{15})')
    palindromes = set()
    for match in re.finditer(pattern, text):
        palindrome = match.group(1)
        if palindrome not in palindromes:
            palindromes.add(palindrome)
    return palindromes