def palindrome_of_length_at_least_n(string):
    """
            Finds all palindromes of the length greater than or equal to 96 that exist in the given string.
            """
    palindromes = set()
    string = string.lower()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                if len(substring) >= 96:
                    palindromes.add(substring)
    return palindromes