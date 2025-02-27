def is_palindrome(word):
    word = ''.join(filter(str.isalpha, word.lower()))
    return word == word[::-1]

def palindrome_of_length_at_least_n(word, n=14):
    if n < 1:
        raise ValueError('n must be a positive integer')
    palindromes = {word[i:j] for word in word.split() for i in range(len(word)) for j in range(i, min(i + n, len(word) + 1)) if is_palindrome(word[i:j])}
    return palindromes