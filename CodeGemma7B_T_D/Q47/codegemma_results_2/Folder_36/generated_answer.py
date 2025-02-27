def palindromes_of_specific_lengths(s):
    """
    Finds all palindromes of specific lengths in a string, given a range of indices and lengths.

    Args:
      s: The input string.

    Returns:
      A set of all palindromes with the specified requirements.
    """
    s = s.lower()
    palindromes = set()
    start_index = 124
    end_index = 283
    for i in range(start_index, end_index + 1):
        for j in range(i + 115, i + 135):
            if s[i:j] == s[j - 1:i - 1:-1]:
                palindromes.add(s[i:j])
    return palindromes