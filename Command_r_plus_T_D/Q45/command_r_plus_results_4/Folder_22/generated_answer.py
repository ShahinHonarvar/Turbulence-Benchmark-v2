def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    palindromes = set()
    for i in range(5, min(6, len(s)) + 1):
        substring = s[i:i + 1]
        if substring.isalpha():
            palindromes.add(substring.lower())
    for i in range(5, min(7, len(s))):
        substring = s[i:i + 2]
        if substring.isalpha() and substring.lower() == substring[::-1].lower():
            palindromes.add(substring.lower())
    return palindromes