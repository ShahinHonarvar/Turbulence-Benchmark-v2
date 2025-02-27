def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word.lower() == word.lower()[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join((c for c in s if c.isalpha()))
    s_english_letters = get_english_letters(s[4:8])
    if len(s_english_letters) < 5:
        return set()
    palindromes = set()
    for i in range(len(s_english_letters) - 4):
        for j in range(i + 1, len(s_english_letters) - 4 + i):
            substring = s_english_letters[i:j]
            for k in range(j + 1, len(s_english_letters) + 1):
                word = substring + s_english_letters[j:k][::-1]
                if is_palindrome(word) and len(word) >= 5:
                    palindromes.add(word)
    return palindromes