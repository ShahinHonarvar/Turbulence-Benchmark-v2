def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 172):
        substring = text[i:i + 173].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes