def palindromes_between_indices(string):

    def is_palindrome(sub):
        return sub == sub[::-1]
    subStr = string[5:10].lower()
    palindromes = set()
    for i in range(4, len(subStr) + 1):
        for comb in combinations(subStr, i):
            for perm in permutations(comb):
                word = ''.join(perm)
                if is_palindrome(word):
                    palindromes.add(word)
    return palindromes