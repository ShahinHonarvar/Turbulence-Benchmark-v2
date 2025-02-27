from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(string):

    def is_palindrome(word):
        return word == word[::-1]
    result = set()
    for i in range(len(string) - 3):
        for j in range(i + 4, len(string) + 1):
            for permutation in permutations(ascii_lowercase[:len(string[i:j])]):
                if is_palindrome(''.join(permutation)):
                    result.add(''.join(permutation))
    return result