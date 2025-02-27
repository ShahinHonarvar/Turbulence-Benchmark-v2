def palindromes_of_specific_lengths(text):
    """
    This function takes one argument, a string.
    The given string may consist of any character.
    The function should return the set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 0 to index 50, both inclusive, should be considered.
    Only palindromes of lengths between 50 to 100 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    text = text.lower()
    palindromes = set()
    for i in range(50):
        for j in range(25):
            if text[i:i + j + 1] == text[i:i + j + 1][::-1]:
                palindromes.add(text[i:i + j + 1])
            if len(text) >= i + 100:
                if text[i:i + j + 1] == text[i:i + j + 1][::-1]:
                    palindromes.add(text[i:i + j + 1])
    return palindromes