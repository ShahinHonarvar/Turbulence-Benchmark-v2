def palindromes_of_specific_lengths(text):
    """
  Only palindromes occurring in the substring from index 14 to index 90, both inclusive, should be considered.
  Only palindromes of lengths between 55 to 71 (both inclusive) should be considered.
  Each palindrome should only consist of English letters.
  """
    start_index = 14
    end_index = 90
    min_len = 55
    max_len = 71
    result_set = set()
    text = text.lower()
    for i in range(start_index, end_index + 1):
        for j in range(i, end_index + 1):
            substring = text[i:j + 1]
            if len(substring) >= min_len and len(substring) <= max_len and (substring == substring[::-1]):
                result_set.add(substring)
    return result_set