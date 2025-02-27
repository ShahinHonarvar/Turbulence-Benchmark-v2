def palindrome_of_length_at_least_n(txt):
    """
  Returns a set of palindromes of length greater than or equal to 62 that exist in the given string.
  Each palindrome should only consist of English letters. If no such palindromes exist in the given string, the function should return an empty set.
  The function should find the palindromes in a case-insensitive manner.
  """
    palindromes = set()
    for W in txt.lower():
        if W.isalpha() and txt.lower().endswith(W):
            for L in txt.lower():
                if L == W:
                    continue
                if txt.lower().endswith(W + L + W):
                    word = W + L + W
                    if len(word) >= 62:
                        palindromes.add(word)
        for L in txt.lower():
            if L == W:
                continue
            for R in txt.lower():
                if R == W or R == L:
                    continue
                if txt.lower().endswith(W + R + L + R + W):
                    word = W + R + L + R + W
                    if len(word) >= 62:
                        palindromes.add(word)
    return palindromes