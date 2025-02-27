def palindrome_of_length_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 92, len(text) + 1):
            subtext = text[i:j]
            if subtext == subtext[::-1]:
                palindromes.add(subtext)
    return palindromes