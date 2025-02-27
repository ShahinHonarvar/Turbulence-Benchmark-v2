def palindromes_between_indices(input_string: str) -> set:

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    english_letters = ''.join(filter(str.isalpha, input_string[1:4]))
    for i in range(1, len(english_letters) + 1):
        for perm in set(permutations(english_letters, i)):
            perm_str = ''.join(perm).lower()
            if is_palindrome(perm_str) and len(perm_str) >= 4:
                palindromes.add(perm_str)
    return palindromes