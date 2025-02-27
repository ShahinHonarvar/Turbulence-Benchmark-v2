def palindromes_of_specific_lengths(text):
    """
    This function takes a string as input and returns a set of all palindromes with the following requirements:
    Only palindromes occurring in the substring from index 0 to index 6, both inclusive, should be considered.
    Only palindromes of lengths between 3 to 6 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 3, min(i + 7, len(text))):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                palindromes.add(text[i:j + 1])
    return palindromes