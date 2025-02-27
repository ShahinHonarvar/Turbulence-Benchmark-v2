from collections import defaultdict

def palindromes_between_indices(s):
    en_letters = {chr(i).lower() for i in range(ord('a'), ord('z') + 1)}
    letters = {letter for letter in en_letters if s[2:5].lower().count(letter) > 0}
    if len(letters) < 2:
        return set()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = {word for word in {letters[i] + letter for letter in letters for i in range(5)} if is_palindrome(word)}
    for _ in range(2, len(letters) - 1):
        palindromes.update({word for word in {letters[i] + word + letters[i] for word in palindromes for i in range(5)} if is_palindrome(word) & (len(word) > 2)})
    return {word for word in palindromes if set(word) <= en_letters}