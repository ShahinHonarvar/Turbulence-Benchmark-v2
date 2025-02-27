def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    english_letters = get_english_letters(s[1:8])
    if len(english_letters) < 7:
        return set()
    all_palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 7, len(english_letters) + 1):
            sub_str = english_letters[i:j]
            if is_palindrome(sub_str):
                all_palindromes.add(sub_str)
    return all_palindromes