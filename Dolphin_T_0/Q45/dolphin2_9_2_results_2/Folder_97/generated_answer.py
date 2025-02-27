def palindromes_between_indices(s):

    def is_palindrome(w):
        return w == w[::-1]
    chars = set()
    for i in range(5):
        chars.add(s[i].lower())
    palindromes = set()
    for char_count in range(3, len(chars) + 1):
        for chars_comb in combinations(chars, char_count):
            for perm in permutations(chars_comb):
                word = ''.join(perm)
                if is_palindrome(word):
                    palindromes.add(word)
    return palindromes