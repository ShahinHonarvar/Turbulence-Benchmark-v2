def palindrome_of_length_n(text):
    text = text.lower()
    text = ''.join(filter(str.isalpha, text))
    palindromes = set()
    for i in range(len(text) - 406):
        for j in range(i + 407):
            word = text[i:j]
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes