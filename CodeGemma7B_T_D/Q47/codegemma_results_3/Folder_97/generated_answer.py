def palindromes_of_specific_lengths(s):
    """
    Write a function called 'palindromes_of_specific_lengths' that takes one argument, a string.
    The given string may consist of any character. The function should return the set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 28 to index 94, both inclusive, should be considered.
    Only palindromes of lengths between 38 to 49 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """

    def is_palindrome(substr):
        return substr == substr[::-1]
    s = s.lower()
    palindromes = set()
    for i in range(28, 95):
        for j in range(38, 50):
            if is_palindrome(s[i:i + j]):
                palindromes.add(s[i:i + j])
    return palindromes