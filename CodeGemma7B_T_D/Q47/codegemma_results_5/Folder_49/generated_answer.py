def palindromes_of_specific_lengths(text):
    if len(text) < 20 or len(text) > 100:
        return set()
    text = text.lower()
    palindromes = set()
    for i in range(10, 100):
        for j in range(i + 10, 100):
            palindrome = text[i:j + 1]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes