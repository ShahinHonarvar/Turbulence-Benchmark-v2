def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    english_letters = get_english_letters(s[:6])
    if len(english_letters) < 5:
        return set()
    palindromes = set()
    for i in range(len(english_letters) - 4):
        for j in range(i + 1, len(english_letters) - i):
            window = english_letters[i:j]
            for k in range(j, i, -1):
                palindrome = window + english_letters[k]
                if len(palindrome) >= 5 and is_palindrome(palindrome):
                    palindromes.add(palindrome)
    return palindromes