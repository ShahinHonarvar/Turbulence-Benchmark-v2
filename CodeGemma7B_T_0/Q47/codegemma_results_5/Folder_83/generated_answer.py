def palindromes_of_specific_lengths(text):
    """
    This function takes a string as input and returns a set of all palindromes with the following requirements:
    - Only palindromes occurring in the substring from index 75 to index 95, both inclusive, should be considered.
    - Only palindromes of lengths between 7 to 9 (both inclusive) should be considered.
    - Each palindrome should only consist of English letters.
    - If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    - The function should find the palindromes in a case-insensitive manner.
    """
    text = text.lower()
    palindromes = set()
    for i in range(75, 96):
        for j in range(i + 6, 96):
            substring = text[i:j + 1]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes