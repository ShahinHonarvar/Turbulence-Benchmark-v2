def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def get_palindromes():
        for i in range(3, len(s) + 1):
            for j in combinations(s, i):
                string_j = ''.join(j)
                if is_palindrome(string_j):
                    yield string_j
    return set(get_palindromes())