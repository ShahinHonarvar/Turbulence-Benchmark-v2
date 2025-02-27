def palindromes_between_indices(s: str) -> set:

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    substring = s[5:10].lower()
    for i in range(len(substring)):
        for j in range(i + 5, len(substring) + 1):
            if is_palindrome(substring[i:j]):
                palindromes.add(substring[i:j])
    return palindromes