def palindrome_of_length_at_least_n(text):
    """
            Write a function called 'palindrome_of_length_at_least_n' that takes one argument, a string, and returns the set of all palindromes of the length greater than or equal to 122 that exist in the given string. Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set. The function should find the palindromes in a case-insensitive manner.
            """
    if not text or len(text) < 122:
        return set()
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 122, len(text) + 1):
            palindrome = text[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes