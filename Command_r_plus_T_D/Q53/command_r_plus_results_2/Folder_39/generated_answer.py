def palindrome_of_length_at_least_n(s: str) -> set:

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    palindromes = set()
    words = s.split()
    for word in words:
        if is_palindrome(word) and len(word) >= 69:
            palindromes.add(word)
    return palindromes