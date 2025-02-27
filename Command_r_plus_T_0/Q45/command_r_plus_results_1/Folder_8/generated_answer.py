def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    english_letters = get_english_letters(s[1:6])
    if len(english_letters) < 5:
        return set()
    all_palindromes = set()
    for i in range(len(english_letters) - 4):
        for j in range(i + 1, len(english_letters) - 3):
            for k in range(j + 1, len(english_letters) - 2):
                for l in range(k + 1, len(english_letters) - 1):
                    for m in range(l + 1, len(english_letters)):
                        palindrome = english_letters[i:m + 1]
                        if is_palindrome(palindrome):
                            all_palindromes.add(palindrome)
    return all_palindromes