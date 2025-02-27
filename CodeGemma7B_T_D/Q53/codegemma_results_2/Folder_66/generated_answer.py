def palindrome_of_length_at_least_n(text):
    """
            Returns set of all palindrome in text of lenght >= n
            """
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 76, len(text)):
            if text[i:j + 1] == text[j:i:-1]:
                palindromes.add(text[i:j + 1].lower())
    return palindromes