def palindrome_of_length_n(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word.lower() == word.lower()[::-1]
    length = 51
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s) - length + 1):
        substring = s_lower[i:i + length]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes