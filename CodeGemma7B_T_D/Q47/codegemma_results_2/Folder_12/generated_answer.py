def palindromes_of_specific_lengths(str_in):
    """
  This function returns the set of all palindromes with the specified requirements.
  """
    str_in = str_in.lower()
    palindromes = set()
    for i in range(62, 89):
        for j in range(18, 22):
            substring = str_in[i:i + j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    if not palindromes:
        return set()
    return palindromes