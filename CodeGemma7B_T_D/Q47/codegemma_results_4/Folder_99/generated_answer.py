def palindromes_of_specific_lengths(string):
    """
            Finds all palindromes with the specified requirements.
            """
    palindromes = set()
    for i in range(127, 288 + 1):
        for j in range(i - 141, i - 119 - 1, -1):
            if string[i] == string[j] and string[j + 1:i + 1] == string[j + 1:i + 1][::-1]:
                palindromes.add(string[j + 1:i + 1])
    return palindromes