def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    return {word for word in (s[i:i + j] for i in range(300) for j in range(50, 61)) if is_palindrome(word.lower())}