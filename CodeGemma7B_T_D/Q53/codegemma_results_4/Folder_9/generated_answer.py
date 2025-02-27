def palindrome_of_length_at_least_n(text):
    palindromes = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 94, len(text) + 1):
            palindrome = text[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes