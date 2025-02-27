def palindromes_of_specific_lengths(text):
    """
    This function takes a string as an argument and returns the set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 18 to index 65, both inclusive, should be considered.
    Only palindromes of lengths between 23 to 36 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    text = text.lower()
    for i in range(18, 66):
        for j in range(i - 22, i + 1):
            if j >= 0 and j < len(text) and (text[i] == text[j]):
                palindrome = text[j:i + 1]
                if len(palindrome) >= 23 and len(palindrome) <= 36 and palindrome.isalpha():
                    palindromes.add(palindrome)
    return palindromes