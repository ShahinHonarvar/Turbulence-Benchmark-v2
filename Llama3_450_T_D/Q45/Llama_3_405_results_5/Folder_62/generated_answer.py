import itertools

def palindromes_between_indices(s):
    s = s[:9].lower()
    english_letters = [char for char in s if char.isalpha()]
    distinct_letters = set(english_letters)
    palindromes = set()
    for length in range(7, len(english_letters) + 1):
        for combination in itertools.combinations(english_letters, length):
            for permutation in itertools.permutations(combination):
                palindrome = ''.join(permutation)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes