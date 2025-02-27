import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[1:8])
    letters = [letter.lower() for letter in letters]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, left, right):
        if is_palindrome(current) and len(current) >= 6:
            palindromes.add(current)
        if left > 0:
            generate_palindromes(current + letters[left - 1], left - 1, right)
        if right < len(letters):
            generate_palindromes(current + letters[right], left, right + 1)
    generate_palindromes('', len(letters), 0)
    return palindromes