def palindromes_of_specific_lengths(string):
    """
    >>> palindromes_of_specific_lengths("Madam I'm Adam")
    {'MADAM', 'ADAM'}
    >>> palindromes_of_specific_lengths("Able was I ere I saw Elba")
    {'ELBA'}
    >>> palindromes_of_specific_lengths("Redivider")
    {'RED'}
    >>> palindromes_of_specific_lengths("Test. Case. Test!")
    set()
    """
    string = ''.join((char for char in string.lower() if char.isalpha()))
    palindromes = set()
    for i in range(11, 84):
        for j in range(i, 84):
            substring = string[i:j + 1]
            if substring == substring[::-1] and 37 <= len(substring) <= 60:
                palindromes.add(substring.upper())
    return palindromes