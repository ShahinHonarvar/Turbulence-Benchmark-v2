def palindromes_of_specific_lengths(text):
    """
            This function takes one argument, a string.
            The given string may consist of any character.
            The function should return the set of all palindromes with the following requirements.
            Only palindromes occurring in the substring from index 17 to index 95, both inclusive, should be considered.
            Only palindromes of lengths between 13 to 49 (both inclusive) should be considered.
            Each palindrome should only consist of English letters.
            If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
            The function should find the palindromes in a case-insensitive manner.
            """
    palindrome = set()
    for i in range(17, 96):
        for j in range(i, 96):
            temp = text[i:j + 1]
            if temp == temp[::-1] and temp.isalpha():
                palindrome.add(temp.lower())
    return palindrome