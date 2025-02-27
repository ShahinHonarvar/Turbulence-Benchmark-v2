def palindromes_of_specific_lengths(text):
    """
        Write a function called 'palindromes_of_specific_lengths' that takes one argument, a string.
        The given string may consist of any character.
        The function should return the set of all palindromes with the following requirements.
        Only palindromes occurring in the substring from index 13 to index 95, both inclusive, should be considered.
        Only palindromes of lengths between 57 to 60 (both inclusive) should be considered.
        Each palindrome should only consist of English letters.
        If no such palindrome with the length specified occurs in the specified index range,
        the function should return an empty set.
        The function should find the palindromes in a case-insensitive manner.
    """
    result = set()
    text = text.lower()
    for i in range(13, 96):
        for j in range(i + 57, i + 61):
            if text[i:j + 1] == text[i:j + 1][::-1]:
                result.add(text[i:j + 1])
    return result