def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]

    def get_english_letters(text):
        return ''.join(filter(str.isalpha, text)).lower()
    s_english_letters = get_english_letters(s[4:9])
    if len(s_english_letters) < 6:
        return set()
    all_palindromes = set()
    for i in range(len(s_english_letters)):
        for j in range(i + 6, len(s_english_letters) + 1):
            palindrome = s_english_letters[i:j]
            if is_palindrome(palindrome):
                all_palindromes.add(palindrome)
    return all_palindromes