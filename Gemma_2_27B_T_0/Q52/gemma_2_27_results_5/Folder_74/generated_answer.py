def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 95):
        substring = text[i:i + 96].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(text[i:i + 96])
    return palindromes