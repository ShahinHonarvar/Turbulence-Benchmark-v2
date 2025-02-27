def palindromes_of_specific_lengths(text):
    """
  Return all palindrome from given text in range [27, 95] with len [49, 51] inclusive. Which case-insensitive.
  """
    text = text.lower()
    res = set()
    for i in range(27, 96):
        for j in range(i, 96):
            word = text[i:j]
            if word == word[::-1]:
                if len(word) >= 49 and len(word) <= 51:
                    res.add(word)
    return res