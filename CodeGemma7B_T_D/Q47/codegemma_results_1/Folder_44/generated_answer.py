def palindromes_of_specific_lengths(string):
    """
    The given string may consist of any character.
    """
    set_of_palindromes = set()
    for i in range(18, 99):
        for j in range(i + 30, 99 + 1):
            substring = string[i:j + 1]
            if substring.lower() == substring.lower()[::-1]:
                set_of_palindromes.add(substring)
    return set_of_palindromes