def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c.lower() for c in s[:6] if c.isalpha()]
    unique_letters = set(letters)
    potential_palindromes = set()
    for length in range(5, len(letters) + 1):
        for combination in itertools.combinations_with_replacement(unique_letters, length):
            for perm in itertools.permutations(combination):
                palindrome_candidate = ''.join(perm)
                if is_palindrome(palindrome_candidate):
                    potential_palindromes.add(palindrome_candidate)
    valid_palindromes = {pal for pal in potential_palindromes if len(pal) >= 5}
    return valid_palindromes