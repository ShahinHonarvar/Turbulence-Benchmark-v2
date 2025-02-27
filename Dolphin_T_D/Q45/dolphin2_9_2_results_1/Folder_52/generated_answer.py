def palindromes_between_indices(string):
    sub_string = string[:8]
    sub_string = ''.join(sorted(sub_string))
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for sub in itertools.combinations(sub_string, 6):
        for p in set(itertools.permutations(sub)):
            if is_palindrome(p):
                palindromes.add(''.join(p).lower())
    return palindromes