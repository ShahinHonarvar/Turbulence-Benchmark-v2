def palindrome_of_length_n(text):
    palindrome = set()
    for i in range(len(text)):
        for j in range(i + 28, len(text)):
            word = text[i:j + 1]
            if word == word[::-1] and word.isalpha():
                palindrome.add(text[i:j + 1])
    return palindrome