def palindrome_of_length_n(text):
    """
    Write a function called 'palindrome_of_length_n' that takes one argument, a string, and returns the set of all palindromes of the length equal to 16, where each palindrome is a substring of the given string. Each palindrome should only consist of English letters. If there is no palindrome of the specified length as a substring of the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
    """
    text_lower = text.lower()
    palindromes = set()
    for i in range(len(text_lower)):
        for j in range(i + 16, len(text_lower) + 1):
            substring = text_lower[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes