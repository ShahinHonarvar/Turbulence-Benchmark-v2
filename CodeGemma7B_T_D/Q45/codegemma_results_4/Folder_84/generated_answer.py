from itertools import permutations

def palindromes_between_indices(string):

    def is_palindrome(word):
        return word == word[::-1]
    filtered_letters = [char.lower() for char in string[4:10] if char.isalpha()]
    if not filtered_letters:
        return set()
    palindromes = set()
    for permutation in permutations(filtered_letters):
        for i in range(len(permutation) - 2):
            palindrome = ''.join(permutation[i:i + 3])
            if is_palindrome(palindrome):
                palindromes.add(palindrome)
    return palindromes