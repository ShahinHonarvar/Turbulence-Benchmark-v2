def palindromes_of_specific_lengths(txt):
    """
    Finds the set of palindromes in the substring from index 23 to index 77, both inclusive,
    that are of lengths between 13 to 40 (both inclusive) and consist of English letters.
    """

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    lower_txt = txt.lower()
    for i in range(23, 78):
        for j in range(i + 13, i + 41):
            substring = lower_txt[i:j]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes