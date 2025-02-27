def palindromes_of_specific_lengths(s):
    """
    Write a function called 'palindromes_of_specific_lengths' that takes one argument, a string.
    The given string may consist of any character.
    The function should return the set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 24 to index 97, both inclusive, should be considered.
    Only palindromes of lengths between 10 to 36 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    palindromes = set()
    for i in range(24, 98):
        for j in range(i + 10, i + 37):
            substring = s[i:j].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes