def palindrome_of_length_at_least_n(str):
    """Given a string, return the set of all palindromes of length
        greater than or equal to 92.
    """
    str = str.lower()
    palindromes = set()
    for i in range(len(str)):
        for j in range(i + 92, len(str)):
            substring = str[i:j + 1]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes