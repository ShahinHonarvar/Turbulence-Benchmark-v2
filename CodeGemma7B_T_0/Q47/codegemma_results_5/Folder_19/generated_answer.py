def palindromes_of_specific_lengths(text):
    """
    This function takes a string and returns the set of all palindromes with the following requirements:
    Only palindromes occurring in the substring from index 10 to index 55, both inclusive, should be considered.
    Only palindromes of lengths between 3 to 7 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    text = text.lower()
    palindromes = set()
    for i in range(10, 56):
        for j in range(i + 1, min(i + 8, 56)):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes