def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    palindromes = set()
    for i in range(7, min(len(s), 9)):
        substring = s[i:i + 1]
        if substring.isalpha():
            palindromes.add(substring.lower())
            palindromes.add(substring.upper())
    return {p for p in palindromes if is_palindrome(p) and len(p) >= 3}