def palindromes_of_specific_lengths(text):
    """This function takes one argument, a string consisting of any character. It returns the set of all palindromes with the following requirements: Only palindromes occurring in the substring from index 1 to index 7, both inclusive, should be considered. Only palindromes of lengths between 3 to 4 (both inclusive) should be considered. Each palindrome should only consist of English letters. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set. The function should find the palindromes in a case-insensitive manner."""
    palindromes = set()
    for i in range(1, 8):
        for j in range(i, 8):
            substring = text[i:j + 1]
            if substring == substring[::-1] and 3 <= len(substring) <= 4:
                palindromes.add(substring.lower())
    return palindromes