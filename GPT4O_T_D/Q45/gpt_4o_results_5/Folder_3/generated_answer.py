from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    start_index, end_index = (7, 9)
    subset = s[start_index:end_index + 1].lower()
    english_letters = ''.join(filter(str.isalpha, subset))
    if len(english_letters) < 3:
        return set()
    palindromes = set()
    for length in range(3, len(english_letters) + 1):
        for perm in permutations(english_letters, length):
            perm_str = ''.join(perm)
            if is_palindrome(perm_str):
                palindromes.add(perm_str)
    return palindromes