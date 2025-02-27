def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 26):
        substring = text[i:i + 27].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(text[i:i + 27])
    return palindromes