def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def get_english_letters(s: str) -> str:
        return ''.join(filter(str.isalpha, s)).lower()
    s = s[:7]
    english_letters = get_english_letters(s)
    unique_letters = set(english_letters)
    palindromes = set()
    for letter in unique_letters:
        if english_letters.count(letter) >= 2:
            palindromes.add(letter * 2)
    for i in range(len(unique_letters)):
        for j in range(i + 1, len(unique_letters)):
            letter_pair = unique_letters[i] + unique_letters[j]
            if english_letters.count(unique_letters[i]) >= 1 and english_letters.count(unique_letters[j]) >= 1:
                palindromes.add(letter_pair)
    return {p for p in palindromes if is_palindrome(p) and len(p) >= 3}