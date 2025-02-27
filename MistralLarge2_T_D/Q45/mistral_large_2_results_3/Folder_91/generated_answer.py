def palindromes_between_indices(s):
    substring = ''.join((c for c in s[2:7] if c.isalpha())).lower()
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for length in range(3, len(substring) + 1):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes