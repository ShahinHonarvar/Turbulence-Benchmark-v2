def palindromes_between_indices(str):

    def is_palindrome(word):
        return word == word[::-1]
    result = set()
    for combination in itertools.permutations(str[3:8]):
        combination = ''.join(combination).lower()
        if is_palindrome(combination) and len(combination) >= 5:
            result.add(combination)
    return result