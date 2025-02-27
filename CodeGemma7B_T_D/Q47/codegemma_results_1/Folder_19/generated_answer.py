def palindromes_of_specific_lengths(s):
    """
    Returns the set of all palindromes of lengths between 3 to 7 (inclusive) that occur
    in the substring from index 10 to index 55, both inclusive.
    """
    palindromes = set()
    s = s.lower()
    for i in range(10, 56):
        for j in range(i - 3, i + 4):
            if j - i <= 0 or j - i >= 5:
                continue
            if s[i - j] == s[i + j - i - 1]:
                palindromes.add(s[i - j:i + j - i - 1])
    return palindromes