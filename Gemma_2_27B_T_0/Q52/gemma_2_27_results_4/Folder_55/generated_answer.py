def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 96):
        substring = text[i:i + 97].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(text[i:i + 97])
    return palindromes