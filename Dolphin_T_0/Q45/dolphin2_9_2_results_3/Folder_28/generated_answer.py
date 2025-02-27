def palindromes_between_indices(s):
    letters = [ch for ch in s[1:6] if ch.isalpha()]
    palindromes = set()

    def check_palindrome(word):
        return word == word[::-1]
    if len(letters) >= 2:
        permutations = [''.join(p) for p in permutations(letters)]
        for p in permutations:
            if len(p) >= 4 and check_palindrome(p):
                palindromes.add(p)
    return palindromes