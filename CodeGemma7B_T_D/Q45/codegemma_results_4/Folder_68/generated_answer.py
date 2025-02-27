def palindromes_between_indices(s):
    """Returns the set of all palindromes of the length of at least 4 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 1 to index 8, both inclusive. If no such palindromes of the specified length can be created from the English letters of the given string that occur in the specified range, the function should return an empty set. The function should form each palindrome in a case-insensitive manner."""
    pale = set()
    for i in range(1, len(s)):
        for j in range(i + 1, len(s)):
            for k in range(j + 1, len(s)):
                for l in range(k + 1, len(s) + 1):
                    word = s[i - 1:l + 1].lower()
                    if word == word[::-1] and len(word) >= 4:
                        pale.add(word)
    return pale