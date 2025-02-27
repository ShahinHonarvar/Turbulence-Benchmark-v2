def palindrome_of_length_n(text):
    palindromes = set()
    for i in range(len(text) - 18):
        substring = text[i:i + 19].lower()
        if substring == substring[::-1]:
            palindromes.add(text[i:i + 19])
    return palindromes