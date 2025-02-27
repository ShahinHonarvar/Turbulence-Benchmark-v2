def palindromes_of_specific_lengths(string):
    """
    Returns the set of all palindromes with the following requirements:
    Only palindromes occurring in the substring from index 13 to index 99, both inclusive, should be considered.
    Only palindromes of lengths between 26 to 29 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    """
    palindromes = set()
    string = string.lower()
    for i in range(13, 99 + 1):
        for j in range(26, 29 + 1):
            substring = string[i - j:i]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes