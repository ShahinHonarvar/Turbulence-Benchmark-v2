def palindrome_of_length_n(text):
    palindromes = set()
    text = text.lower()
    for i in range(len(text) - 172):
        substring = text[i:i + 173]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes