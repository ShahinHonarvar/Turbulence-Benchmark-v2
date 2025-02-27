def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 130):
        substring = text[i:i + 131]
        if substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes