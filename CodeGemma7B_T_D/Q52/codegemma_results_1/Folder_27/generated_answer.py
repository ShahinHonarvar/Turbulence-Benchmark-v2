def palindrome_of_length_n(string):
    """
    Checks if the given sting contains palindromes of the length equals to n.
    """
    palindrome_set = set()
    string = string.lower()
    for start in range(len(string) - 55):
        for end in range(start + 56, len(string) + 1):
            substring = string[start:end]
            if substring == substring[::-1]:
                palindrome_set.add(substring)
    return palindrome_set