def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def generate_palindromes(s):
        palindromes = set()
        for word in (''.join(p) for p in permutations(s)):
            if len(word) >= 3 and is_palindrome(word):
                palindromes.add(word.lower())
        return palindromes
    return generate_palindromes(s[5:9])