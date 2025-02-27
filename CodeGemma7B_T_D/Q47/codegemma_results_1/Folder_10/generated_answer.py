def palindromes_of_specific_lengths(str):
    """Returns the set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 16 to index 60, both inclusive, should be considered.
    Only palindromes of lengths between 16 to 39 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner."""
    return {word for word in map(str.lower, str[16:61].split()) if word == word[::-1] and 16 <= len(word) <= 39}