import itertools

def palindromes_between_indices(s):
    s = s[1:6]
    letters = [c for c in s if c.isalpha()]
    letters = [c.lower() for c in letters]
    unique_letters = set(letters)
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for product in itertools.product(unique_letters, repeat=length):
            p = ''.join(product)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes