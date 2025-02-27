def palindrome_of_length_at_least_n(text):
    palindromes = set()
    text = text.lower()
    n = 63
    for i in range(len(text) - 1):
        for j in range(i + 2, len(text) + 1):
            word = text[i:j]
            if word == word[::-1] and len(word) >= n:
                palindromes.add(word)
    return palindromes