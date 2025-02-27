def palindromes_between_indices(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[2:6]
    unique_chars = ''.join(sorted(set(substring.lower())))
    palindromes = set()
    for length in range(3, len(unique_chars) + 1):
        for chars in unique_chars:
            for perm in permutations(unique_chars, length):
                if is_palindrome(''.join(perm)):
                    palindromes.add(''.join(perm))
    return palindromes