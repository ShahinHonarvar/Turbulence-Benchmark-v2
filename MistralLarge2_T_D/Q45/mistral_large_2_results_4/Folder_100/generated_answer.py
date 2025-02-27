def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    subset = ''.join(filter(str.isalpha, s[:6])).lower()
    palindromes = set()
    for length in range(6, len(subset) + 1):
        for i in range(len(subset) - length + 1):
            substring = subset[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes