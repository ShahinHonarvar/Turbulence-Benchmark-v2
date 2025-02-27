def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.lower() in 'abcdefghijklmnopqrstuvwxyz'))
    english_letters = get_english_letters(s[4:10])
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 7, len(english_letters) + 1):
            sub_str = english_letters[i:j]
            if is_palindrome(sub_str):
                palindromes.add(sub_str)
    return palindromes