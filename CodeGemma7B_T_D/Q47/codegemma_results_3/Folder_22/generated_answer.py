def palindromes_of_specific_lengths(text):
    """ Returns a set of palindromes in a case-insensitive manner, from indices
  100 to 200, inclusive, with lengths between 5 and 10, inclusive.
  """
    text = text.lower()
    result = set()
    for i in range(100, 201):
        for j in range(i - 4, i + 1):
            if j > 0 and j <= len(text) and (text[j] != text[i]):
                continue
            palindrome = text[i]
            for c in range(j - 1, 0, -1):
                if text[c] != text[i]:
                    break
                palindrome = text[c] + palindrome
            result.add(palindrome)
    return result