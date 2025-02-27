def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    possible_palindromes = set()
    subset_string = s[1:9]
    for i in range(1, len(subset_string)):
        for j in range(i + 3, len(subset_string) + 1):
            substring = subset_string[i:j]
            if set(substring).issubset(english_letters) and is_palindrome(substring):
                possible_palindromes.add(substring)
    return {p for p in possible_palindromes if len(p) >= 7}