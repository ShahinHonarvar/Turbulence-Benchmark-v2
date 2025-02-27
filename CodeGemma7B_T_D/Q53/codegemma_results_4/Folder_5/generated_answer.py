def palindrome_of_length_at_least_n(string):
    """
    Finds the set of all palindromes of the length greater than or equal to 46 that exist in the given string.
    """
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 46, len(string) + 1):
            if string[i:j] == string[j - 1:i - 1:-1]:
                palindromes.add(string[i:j])
    return palindromes