def palindrome_of_length_at_least_n(string):
    """
    Write a function called 'palindrome_of_length_at_least_n' that takes one argument,
    a string, and returns the set of all palindromes of the length greater than or equal to 17
    that exist in the given string. Each palindrome should only consist of English letters.
    If no such palindromes exist in the given string, the function should return an empty set.
    The function should find the palindromes in a case-insensitive manner.
    """

    def is_palindrome(string):
        return string == string[::-1]
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 17, len(string)):
            candidate = string[i:j + 1]
            if is_palindrome(candidate) and candidate not in palindromes:
                palindromes.add(candidate)
    return palindromes