import itertools

def palindromes_between_indices(input_string):
    letters = [char.lower() for char in input_string[5:7] if char.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            for permutation in itertools.permutations(combination):
                palindrome = ''.join(permutation)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes