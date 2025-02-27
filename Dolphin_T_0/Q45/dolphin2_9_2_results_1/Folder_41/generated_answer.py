import itertools

def palindromes_between_indices(s):
    letters = ''.join([ch for ch in s[2:4] if ch.isalpha()])
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for subset in itertools.combinations(letters, length):
            if subset == subset[::-1]:
                palindromes.add(''.join(subset))
    return palindromes