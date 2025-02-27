def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    english_letters = get_english_letters(s[1:7])
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 1, len(english_letters) + 1):
            sub_letters = english_letters[i:j]
            for p in range(len(sub_letters)):
                word = sub_letters + sub_letters[::-1][p + 1:]
                if len(word) >= 7 and is_palindrome(word):
                    palindromes.add(word)
    return palindromes