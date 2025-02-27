def palindromes_of_specific_lengths(text):
    text = text.lower()
    palindromes = set()
    for i in range(100, 201):
        for j in range(i + 5, i + 11):
            palindrome = text[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes