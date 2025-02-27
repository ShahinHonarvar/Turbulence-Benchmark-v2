def palindrome_of_length_at_least_n(string):
    """
            Returns a set of all palindromes of the length greater than or equal to 91 that exist in the given string.

            Args:
                string: The input string.

            Returns:
                A set of all palindromes of the length greater than or equal to 91 that exist in the given string. If no such palindromes exist in the given string, the function returns an empty set.
            """
    string = re.sub('[^a-zA-Z]', '', string.lower())
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 91, len(string) + 1):
            palindrome = string[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes