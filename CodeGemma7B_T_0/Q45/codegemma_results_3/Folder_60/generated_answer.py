import re
  from itertools import permutations

def palindromes_between_indices(text):

    def is_palindrome(text):
        return text == text[::-1]

    def get_english_letters(text):
        return re.findall('[a-zA-Z]', text)

    def get_palindromes(text):
        english_letters = get_english_letters(text)
        palindromes = set()
        for i in range(len(english_letters) - 3):
            for j in range(i + 4, len(english_letters) + 1):
                for permutation in permutations(english_letters[i:j]):
                    palindrome = ''.join(permutation)
                    if is_palindrome(palindrome):
                        palindromes.add(palindrome)
        return palindromes
    if not get_english_letters(text)[3:7]:
        return set()
    return get_palindromes(text)