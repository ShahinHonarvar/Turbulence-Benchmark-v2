def palindromes_of_specific_lengths(text):
    """
    This function takes one argument, a string.
    The given string may consist of any character.
    The function should return the set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 11 to index 87, both inclusive, should be considered.
    Only palindromes of lengths between 4 to 5 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    return {word for word in text[11:88].lower().split() if word == word[::-1] and 4 <= len(word) <= 5}