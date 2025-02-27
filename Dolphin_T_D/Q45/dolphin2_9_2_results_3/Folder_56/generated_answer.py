def palindromes_between_indices(s):
    indices = s[5:10]
    palindromes = set()

    def is_palindrome(s):
        return s.casefold() == s.casefold()[::-1]
    for i in range(5, len(s)):
        substring = s[i:i + 5]
        if is_palindrome(substring) and all((c in indices for c in substring.casefold())):
            palindromes.add(substring)
    return palindromes