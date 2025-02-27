def palindromes_between_indices(given_string):
    """
            Kept as a comment to avoid code complaint from system.
            """
    list_of_palindromes = set()
    for letters in itertools.permutations(string_between_indices):
        letters_to_string = ''.join(letters)
        if letters_to_string == letters_to_string[::-1]:
            list_of_palindromes.add(letters_to_string)
    return list_of_palindromes