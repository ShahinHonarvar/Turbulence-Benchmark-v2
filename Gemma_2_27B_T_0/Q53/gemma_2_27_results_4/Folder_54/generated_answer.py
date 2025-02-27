def palindrome_of_length_at_least_n(text):
    palindromes = set()
    for i in range(len(text) - 73):
        substring = text[i:i + 74].lower()
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes