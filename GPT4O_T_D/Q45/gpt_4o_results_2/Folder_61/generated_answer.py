from collections import Counter

def palindromes_between_indices(s):

    def can_form_palindrome(counter, length):
        odd_count = 0
        for count in counter.values():
            if count % 2 != 0:
                odd_count += 1
            if odd_count > 1:
                return False
        return odd_count == 0 if length % 2 == 0 else odd_count == 1
    s = s[:8].lower()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    letter_counter = Counter((char for char in s if char in english_letters))
    result = set()
    str_length = sum(letter_counter.values())
    for length in range(7, str_length + 1):
        if can_form_palindrome(letter_counter, length):
            result.add(length)
    return result