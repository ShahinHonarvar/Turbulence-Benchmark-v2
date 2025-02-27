from collections import Counter
    import itertools

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substr = s[1:5].lower()
    letters = [ch for ch in substr if ch.isalpha()]
    unique_letters = set(letters)
    all_combinations = set()
    for length in range(3, len(letters) + 1):
        for combination in itertools.combinations_with_replacement(unique_letters, length):
            if Counter(combination) <= Counter(letters):
                all_combinations.add(''.join(combination))
    palindromes = {word for word in all_combinations if is_palindrome(word)}
    return palindromes