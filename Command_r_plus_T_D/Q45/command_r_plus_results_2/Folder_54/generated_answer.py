def palindromes_between_indices(s: str) -> set:

    def is_palindrome(s):
        return s == s[::-1]

    def get_english_letters(s):
        return ''.join((c for c in s if c.isalpha())).lower()
    english_letters = get_english_letters(s[4:10])
    if len(english_letters) < 4:
        return set()
    palindromes = set()
    for i in range(len(english_letters) - 3):
        for j in range(i + 1, len(english_letters) - 2):
            substring = english_letters[i:j]
            for k in range(j + 1, len(english_letters) + 1):
                candidate = substring + english_letters[j:k][::-1]
                if is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes