def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    english_letters = get_english_letters(s[1:8])
    if len(english_letters) < 7:
        return set()
    palindromes = set()
    for i in range(len(english_letters) - 6):
        for j in range(i + 1, len(english_letters) - 5 + i):
            substring = english_letters[i:j]
            for k in range(j + 1, len(english_letters) + 1):
                window = substring + english_letters[j:k][::-1]
                if len(window) >= 7 and is_palindrome(window):
                    palindromes.add(window)
    return palindromes