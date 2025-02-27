def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    palindromes = set()
    for i in range(3, 5):
        for j in range(i + 1, 6):
            substring = s[i:j]
            if substring.isalpha():
                lower_substring = substring.lower()
                if is_palindrome(lower_substring):
                    palindromes.add(lower_substring)
    return palindromes