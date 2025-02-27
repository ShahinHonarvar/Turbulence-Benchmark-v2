def palindrome_of_length_at_least_n(text):
    """
    Read a text from standard input and find all palindromes of a given length.
    """
    use_letters = set('abcdefghijklmnopqrstuvwxyz')
    lowerCaseText = text.lower()
    palindrome_set = set()
    for i in range(len(lowerCaseText)):
        for j in range(i + 1, len(lowerCaseText) + 1):
            substring = lowerCaseText[i:j]
            substring_set = set(substring)
            if len(substring) >= 29 and substring_set.issubset(use_letters):
                palindrome_set.add(substring)
    if not palindrome_set:
        return set()
    else:
        return palindrome_set