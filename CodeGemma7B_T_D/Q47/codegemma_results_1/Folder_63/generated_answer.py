def palindromes_of_specific_lengths(string):
    """
    Returns the set of all palindromes with the following requirements. Only palindromes occurring in the substring from index 33 to index 85, both inclusive, should be considered. Only palindromes of lengths between 26 to 31 (both inclusive) should be considered. Each palindrome should only consist of English letters. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    str_lower = string.lower()
    for i in range(33, 86):
        for j in range(i, 32, -1):
            palindrome = str_lower[i:j + 1]
            if len(palindrome) not in range(26, 32):
                continue
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes