def palindromes_between_indices(string):
    substring = string[5:9]
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for i in range(len(substring)):
        for j in range(i, len(substring)):
            for perm in permutations(substring[i:j + 1]):
                if is_palindrome(''.join(perm)) and len(''.join(perm)) >= 3:
                    palindromes.add(''.join(perm)).add(''.join(perm).lower())
    return palindromes