def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 45):
        substring = text[i:i + 46]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes