def palindromes_of_specific_lengths(text):
    """
    The function takes one argument, a string. The given string may consist of any character.
    The function returns the set of all palindromes with the following requirements.
    Only palindromes occurring in the substring from index 18 to index 88, both inclusive, should be considered.
    Only palindromes of lengths between 12 to 14 (both inclusive) should be considered.
    Each palindrome should only consist of English letters.
    If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """
    text = text.lower()
    substring = text[18:89]
    palindrome_regex = re.compile('(?i)([a-z]{12,14})\\\\1')
    palindromes = palindrome_regex.findall(substring)
    return set(palindromes)