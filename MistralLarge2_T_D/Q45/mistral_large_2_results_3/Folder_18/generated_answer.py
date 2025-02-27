import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[1:7])
    letters = ''.join(letters).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(current, left, right):
        if len(current) >= 3 and is_palindrome(current):
            palindromes.add(current)
        if left > 0:
            generate_palindromes(letters[left - 1] + current + letters[left - 1], left - 1, right)
        if right < len(letters):
            generate_palindromes(letters[right] + current + letters[right], left, right + 1)
    for i in range(len(letters)):
        generate_palindromes(letters[i], i, i + 1)
    return palindromes