def palindromes_of_specific_lengths(string):
    """
    Finds all palindromes of specified lengths within a substring of the given string.

    Args:
      string: The input string to search for palindromes in.

    Returns:
      A set of all palindromes meeting the specified criteria, or an empty set if no such palindromes are found.
    """
    string = string.lower()
    start_index = 75
    end_index = 95
    min_length = 7
    max_length = 9
    palindromes = set()
    for i in range(end_index, start_index - 1, -1):
        if not string[i].isalpha():
            continue
        for j in range(i - 1, start_index - 1, -1):
            if string[i] == string[j]:
                substring = string[j:i + 1]
                if min_length <= len(substring) <= max_length:
                    palindromes.add(substring)
    return palindromes