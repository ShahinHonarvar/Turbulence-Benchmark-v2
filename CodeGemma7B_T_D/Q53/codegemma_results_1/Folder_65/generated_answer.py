def palindrome_of_length_at_least_n(word):
    """
            Given a string, returns the set of all palindromes of the length greater than or equal to 15 that exist in the given string.
            Each palindrome should only consist of English letters.
            If no such palindromes exist in the given string, the function should return an empty set.
            The function should find the palindromes in a case-insensitive manner.
            """
    palindromes = set()
    word = word.lower()
    for i in range(len(word)):
        for j in range(i + 15, len(word) + 1):
            substring = word[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes