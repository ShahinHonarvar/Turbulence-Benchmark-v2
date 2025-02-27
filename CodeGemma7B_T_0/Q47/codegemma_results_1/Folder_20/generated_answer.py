import re
    import string

def palindromes_of_specific_lengths(text):
    """
    This function takes a string and returns the set of all palindromes with the following requirements:
    Only palindromes occurring in the substring from index 20 to index 74, both inclusive, should be considered.
    Only palindromes of lengths between 36 to 42 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    pattern = re.compile('(?i)([a-zA-Z]{36,42})')
    palindromes = set()
    for i in range(20, 75):
        for j in range(i + 1, 75):
            substring = text[i:j]
            for palindrome in pattern.findall(substring):
                palindromes.add(palindrome)
    return palindromes