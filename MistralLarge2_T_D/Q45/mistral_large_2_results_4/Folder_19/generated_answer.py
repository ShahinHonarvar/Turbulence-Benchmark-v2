import re

def palindromes_between_indices(s):
    substring = re.sub('[^a-zA-Z]', '', s[1:8]).lower()
    letter_counts = {char: substring.count(char) for char in set(substring)}

    def is_palindrome(word):
        return word == word[::-1]

    def can_form_palindrome(word, letter_counts):
        counter = letter_counts.copy()
        for char in word:
            if counter[char] > 0:
                counter[char] -= 1
            else:
                return False
        return True
    palindromes = set()
    for length in range(7, len(substring) + 1):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate) and can_form_palindrome(candidate, letter_counts):
                palindromes.add(candidate)
    return palindromes