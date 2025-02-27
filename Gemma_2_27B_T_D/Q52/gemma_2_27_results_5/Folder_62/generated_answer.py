def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 187):
        substring = text[i:i + 188]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes