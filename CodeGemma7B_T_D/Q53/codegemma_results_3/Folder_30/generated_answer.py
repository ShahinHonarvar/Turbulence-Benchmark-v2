def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for i in range(len(text)):
        for j in range(i, len(text)):
            word = text[i:j + 1]
            if word == word[::-1] and len(word) >= 16:
                palindromes.add(word)
    return palindromes