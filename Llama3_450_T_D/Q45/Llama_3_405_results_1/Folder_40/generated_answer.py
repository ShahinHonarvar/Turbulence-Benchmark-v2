import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:10] if char.isalpha()]
    letters_set = set(letters)
    possible_palindromes = set()
    for length in range(7, len(letters) + 1):
        for combination in itertools.combinations_with_replacement(letters_set, length // 2):
            palindrome = ''.join(combination) + ('' if length % 2 == 0 else letters[0]) + ''.join(combination[::-1])
            possible_palindromes.add(palindrome)
    return possible_palindromes