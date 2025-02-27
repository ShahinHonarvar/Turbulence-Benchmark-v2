def palindrome_of_length_n(any_string):
    """Function 'palindrome_of_length_n' takes one argument 'any_string'; it returns a set of all palindromes of the length equal to 475.
       If there's no palindrome in 'any_string' it will return an empty set."""
    palindromes = set()
    for i in range(len(any_string) - 474):
        substring = any_string[i:i + 475]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes