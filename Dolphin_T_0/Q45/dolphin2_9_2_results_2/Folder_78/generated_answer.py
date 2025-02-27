def palindromes_between_indices(s):
    substring = s[6:9]
    palindromes = set()

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    for i in range(len(substring)):
        for j in range(i + 2, len(substring) + 1):
            for p in permutations(substring[i:j]):
                word = ''.join(p)
                if is_palindrome(word) and len(word) >= 3:
                    palindromes.add(word)
    return palindromes