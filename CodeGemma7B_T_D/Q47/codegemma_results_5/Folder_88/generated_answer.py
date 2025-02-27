def palindromes_of_specific_lengths(text):
    palindromes = set()
    text = text[11:87].lower()
    for i in range(len(text) - 5):
        for j in range(i + 4, len(text)):
            palindrome = text[i:j + 1]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes