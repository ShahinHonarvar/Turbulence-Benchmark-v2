def palindromes_of_specific_lengths(text):
    """
  Finds palindromes with specific lengths within a substring of a given text.
  Args:
    text: The input text, may consist of any character.
  Returns:
    A set of all palindromes with lengths between 10 and 20 (inclusive) in the substring from index 10 to index 75, both inclusive, or an empty set if no such palindrome exists.
  """
    sub_text = text[10:76].lower()
    palindromes = set()
    for length in range(10, 21):
        for start in range(len(sub_text) - length + 1):
            end = start + length
            if sub_text[start:end] == sub_text[start:end][::-1]:
                palindromes.add(sub_text[start:end])
    return palindromes