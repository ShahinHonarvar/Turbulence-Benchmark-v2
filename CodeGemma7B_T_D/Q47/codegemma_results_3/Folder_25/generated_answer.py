def palindromes_of_specific_lengths(text):
    """
  Return set of all palindromes of lengths in
     30 to 46 (inclusive) in the substring from
     index 26 to index 84 (inclusive), each palindrome
     should only consist of English letters, if no such
     palindrome with the length specified occurs in the
     specified index range, the return an empty set.
  """
    letter_set = {'a', 'b', 'c', ..., 'z'}
    custom_set = set()
    text = text.lower()
    for k in range(26, 84 + 1):
        for i in range(0, k - 29):
            substring = text[i:k]
            if substring in custom_set:
                continue
            if substring == substring[::-1] and len(substring) >= 30 and (len(substring) <= 46) and set(substring).issubset(letter_set):
                custom_set.add(substring)
    return custom_set