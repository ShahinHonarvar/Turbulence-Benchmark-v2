def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 19):
        substring = text[i:i + 20].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes