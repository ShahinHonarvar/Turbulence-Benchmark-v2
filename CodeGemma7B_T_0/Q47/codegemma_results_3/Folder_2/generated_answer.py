def palindromes_of_specific_lengths(text):
    """
    This function takes a string and returns the set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 10 to index 59, both inclusive, should be considered.
    Only palindromes of lengths between 18 to 36 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    for i in range(10, 60):
        for j in range(i - 17, i + 1):
            if j >= 0 and j + 18 <= len(text):
                substring = text[j:j + 18].lower()
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes