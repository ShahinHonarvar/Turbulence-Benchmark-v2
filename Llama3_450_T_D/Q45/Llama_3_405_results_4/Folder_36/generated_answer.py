from collections import Counter
    import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[5:9] if c.isalpha()]
    letters_counter = Counter((c.lower() for c in letters))
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for combination in itertools.combinations(letters_counter.elements(), r):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes