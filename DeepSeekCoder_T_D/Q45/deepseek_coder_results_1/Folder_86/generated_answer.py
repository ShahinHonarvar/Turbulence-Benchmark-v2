def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = ''.join(filter(str.isalpha, s[6:10])).lower()
    palindromes = set()
    n = len(letters)
    for i in range(1 << n):
        subset = ''.join((letters[j] for j in range(n) if i & 1 << j))
        if len(subset) >= 4:
            for perm in set(itertools.permutations(subset)):
                word = ''.join(perm)
                if is_palindrome(word):
                    palindromes.add(word)
    return palindromes