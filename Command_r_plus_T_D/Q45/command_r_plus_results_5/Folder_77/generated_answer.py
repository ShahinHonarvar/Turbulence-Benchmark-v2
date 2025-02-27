def palindromes_between_indices(s: str) -> set:

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]
    palindromes = set()
    for i in range(4, 7):
        for j in range(i + 1, 7):
            substring = s[i:j]
            if substring.isalpha():
                substring = substring.lower()
                if is_palindrome(substring) and len(substring) >= 4:
                    palindromes.add(substring)
    return palindromes