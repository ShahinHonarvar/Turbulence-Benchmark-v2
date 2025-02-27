def palindrome_of_length_at_least_n(input_string):
    """
            This function finds the set of all palindromes of the length greater than or equal to 133 that exist in the given string.
            """
    input_string = input_string.lower()
    palindromes = set()
    for i in range(len(input_string)):
        for j in range(i + 133, len(input_string) + 1):
            substring = input_string[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes