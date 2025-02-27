import itertools

def palindromes_between_indices(string):
    indices = tuple(range(4, 8))
    possible_letters = [char for char in string if char.isalpha()]
    palindromes = set()
    for p in range(5, len(possible_letters) + 1):
        for subset in itertools.combinations(possible_letters, p):
            for palindrome in itertools.permutations(subset):
                palindrome = ''.join(palindrome).lower()
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes