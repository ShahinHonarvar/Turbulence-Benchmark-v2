def palindromes_of_specific_lengths(string):
    """
    This function finds the set of all palindromes with the following requirements:
    Only palindromes occurring in the substring from index 200 to index 300, both inclusive, should be considered.
    Only palindromes of lengths between 10 to 50 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    return {word for word in string.lower().split() if 200 <= string.lower().rfind(word) <= 300 and 10 <= len(word) <= 50 and (word == word[::-1])}