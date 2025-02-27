def palindromes_of_specific_lengths(text):
    """
    This function takes a string as input and returns a set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 15 to index 95, both inclusive, should be considered.
    Only palindromes of lengths between 20 to 66 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    text_lower = text.lower()
    for i in range(15, 96):
        for j in range(i + 20, min(i + 67, 96)):
            substring = text_lower[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes