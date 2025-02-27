def palindromes_of_specific_lengths(s):
    """
        Palindromes of specific lengths from an input string
        """
    s = s.lower()
    palindromes = set()
    for i in range(1, 9):
        for j in range(i + 2, 9):
            substring = s[i:j + 1]
            if substring == substring[::-1] and 3 <= len(substring) <= 4 and substring.isalpha():
                palindromes.add(substring)
    return palindromes