def palindromes_of_specific_lengths(text):
    """
    This function takes a string and returns the set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 0 to index 20, both inclusive, should be considered.
    Only palindromes of lengths between 5 to 80 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    for i in range(20):
        for j in range(i + 5, min(i + 81, 21)):
            substring = text[i:j].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes