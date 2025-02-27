def palindromes_of_specific_lengths(text):
    """
    Returns the set of all palindromes with the following requirements. Only palindromes occurring in the substring from index 26 to index 84, both inclusive, should be considered. Only palindromes of lengths between 30 to 46 (both inclusive) should be considered. Each palindrome should only consist of English letters. If no such palindrome with the length specified occurs in the specified index range, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    splitted = text.lower()
    start, end = (26, 84)
    palindromes = set()
    for i in range(len(splitted) - 2):
        for j in range(i + 3, len(splitted)):
            substring = splitted[i:j]
            if substring == substring[::-1] and len(substring) in range(30, 47) and (start <= i <= j <= end):
                palindromes.add(substring)
    return palindromes