import itertools

def palindromes_between_indices(s):
    letters = [ch for ch in s[4:10] if ch.isalpha()]
    palindrome_set = set()
    for length in range(6, 10):
        for subset in itertools.combinations(letters, length):
            for arrangement in itertools.permutations(subset):
                word = ''.join(arrangement)
                if word == word[::-1]:
                    palindrome_set.add(word)
    return palindrome_set