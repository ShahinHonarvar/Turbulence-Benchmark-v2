def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 58):
        substring = text[i:i + 59].lower()
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes