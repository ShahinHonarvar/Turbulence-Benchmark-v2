import re
  from itertools import permutations

def palindromes_between_indices(text):

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(text):
        return re.findall('[a-zA-Z]', text)

    def get_palindromes(letters):
        palindromes = set()
        for i in range(len(letters) - 5):
            for j in range(i + 6, len(letters) + 1):
                word = ''.join(letters[i:j])
                if is_palindrome(word):
                    palindromes.add(word.lower())
        return palindromes
    letters = get_english_letters(text[2:9])
    if not letters:
        return set()
    return get_palindromes(letters)