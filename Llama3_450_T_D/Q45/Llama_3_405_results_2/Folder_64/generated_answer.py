import itertools

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[4:10] if char.isalpha()]
    unique_letters = set(letters)
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for combination in itertools.combinations(unique_letters, length):
            for permutation in itertools.permutations(combination):
                palindrome = ''.join(permutation)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes