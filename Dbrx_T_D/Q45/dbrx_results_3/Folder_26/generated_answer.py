from collections import defaultdict
    from itertools import product

def palindromes_between_indices(s):
    alphabet = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substring = s[4:7]
    letter_counts = defaultdict(int)
    for letter in substring:
        if letter in alphabet:
            letter_counts[letter] += 1
    odd_counts = sum((count % 2 for count in letter_counts.values()))
    if odd_counts > 3:
        return set()
    arrangements = []
    for count in letter_counts.values():
        if count % 2 == 1:
            arrangements.append((letter,) * (count // 2 + 1))
        else:
            arrangements.append((letter,) * (count // 2))
    palindromes = set()
    for product_ in itertools.product(*arrangements):
        palindrome = ''.join((letter for pair in zip(product_, reversed(product_)) for letter in pair))
        palindromes.add(palindrome.lower())
    for letter in letter_counts:
        if letter_counts[letter] % 2 == 0:
            palindromes.update((palindrome + letter + reversed_palindrome for palindrome in palindromes))
    return palindromes