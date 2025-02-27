def palindromes_of_specific_lengths(text):
    text = text[63:71].lower()
    palindromes = set()
    for length in range(4, 6):
        for i in range(len(text) - length + 1):
            palindrome = text[i:i + length]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes