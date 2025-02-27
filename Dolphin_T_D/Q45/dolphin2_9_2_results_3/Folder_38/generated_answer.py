def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    s = s[3:9].lower()
    palindromes = set()
    for i in range(5, len(s) + 1):
        for word in itertools.permutations(s, i):
            if is_palindrome(''.join(word)):
                palindromes.add(''.join(word))
    return palindromes