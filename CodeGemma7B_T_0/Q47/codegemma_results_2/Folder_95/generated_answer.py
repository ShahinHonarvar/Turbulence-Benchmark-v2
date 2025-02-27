def palindromes_of_specific_lengths(text):
    """
    Finds all palindromes of lengths between 20 to 21 (both inclusive) in the substring from index 12 to index 56, both inclusive, in a case-insensitive manner.

    Args:
      text: The string to search for palindromes in.

    Returns:
      A set of all palindromes of lengths between 20 to 21 (both inclusive) in the specified index range, or an empty set if no such palindrome exists.
    """
    text = text.lower()
    palindromes = set()
    for i in range(12, 57):
        for j in range(i + 20, i + 22):
            if text[i:j] == text[i:j][::-1]:
                palindromes.add(text[i:j])
    return palindromes