def palindrome_of_length_at_least_n(text):
    """
    find palindrome of size greater than or equal to 20
    """
    palindrome = set()
    for i in range(len(text)):
        for j in range(i + 25, len(text) + 1):
            Palindrome = text[i:j]
            Palindrome = ''.join((ch for ch in Palindrome if ch.isalpha()))
            Palindrome = Palindrome.lower()
            if Palindrome == Palindrome[::-1]:
                palindrome.add(Palindrome)
    return palindrome