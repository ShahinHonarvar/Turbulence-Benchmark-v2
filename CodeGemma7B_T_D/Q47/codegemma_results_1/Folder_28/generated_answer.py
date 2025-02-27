def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text.lower()
    for index in range(32, 72):
        for length in range(21, 33):
            palindrome = text[index:index + length]
            if palindrome == palindrome[::-1] and palindrome.isalpha():
                palindromes.add(palindrome)
    return palindromes