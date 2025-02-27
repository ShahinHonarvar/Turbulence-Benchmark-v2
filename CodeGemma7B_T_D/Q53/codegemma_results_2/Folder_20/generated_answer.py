def palindrome_of_length_at_least_n(text):
    """This function takes one argument, a string, and returns the set of all palindromes of the length greater than or equal to 66 that exist in the given string. Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner."""
    text_lower = text.lower()
    palindromes = set()
    for i in range(len(text_lower)):
        for j in range(i + 65, len(text_lower) + 1):
            substring = text_lower[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes