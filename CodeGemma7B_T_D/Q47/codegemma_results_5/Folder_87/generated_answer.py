def palindromes_of_specific_lengths(text):
    """
    This function takes one argument, a string, and returns the set of all palindromes consisting of English letters with specific lengths, found within a substring of the input string.
    """
    text = text.lower()
    if not text.isalpha():
        return set()
    palindromes = set()
    for i in range(11, 94):
        for j in range(i + 2, 94):
            if text[i:j] == text[i:j][::-1]:
                palindromes.add(text[i:j])
    if not palindromes:
        return set()
    return palindromes