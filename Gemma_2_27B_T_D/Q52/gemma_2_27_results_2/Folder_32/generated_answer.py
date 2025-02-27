def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 112):
        substring = text[i:i + 113].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(text[i:i + 113])
    return palindromes