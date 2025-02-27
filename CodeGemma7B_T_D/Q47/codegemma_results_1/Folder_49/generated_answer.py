def palindromes_of_specific_lengths(text):

    def is_palindrome(word):
        return word == word[::-1]
    text = text.lower()
    text = text[10:100]
    palindromes = set()
    for i in range(len(text)):
        for j in range(i + 10, min(i + 51, len(text))):
            word = text[i:j]
            if is_palindrome(word) and word.isalpha():
                palindromes.add(word)
    return palindromes