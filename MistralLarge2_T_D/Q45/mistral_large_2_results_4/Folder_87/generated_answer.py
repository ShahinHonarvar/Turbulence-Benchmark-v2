def palindromes_between_indices(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    subset = ''.join((c for c in s[3:10] if c.isalpha())).lower()
    palindromes = set()
    for length in range(3, len(subset) + 1):
        for i in range(len(subset) - length + 1):
            sub = subset[i:i + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes