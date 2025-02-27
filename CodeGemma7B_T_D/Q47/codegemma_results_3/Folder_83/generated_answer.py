def palindromes_of_specific_lengths(text):
    """
    This function takes one argument, a string. The given string may consist of any character.
    The function should return the set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 75 to index 95, both inclusive, should be considered.
    Only palindromes of lengths between 7 to 9 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.

    """
    palindromes = set()
    text = text.lower()
    sub_string = text[75:96]
    for length in range(7, 10):
        for start in range(len(sub_string) - length + 1):
            end = start + length
            if sub_string[start:end] == sub_string[start:end][::-1]:
                palindromes.add(sub_string[start:end])
    return palindromes