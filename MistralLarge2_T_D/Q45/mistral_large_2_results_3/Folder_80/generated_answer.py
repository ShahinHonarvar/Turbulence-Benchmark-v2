import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[3:9] if c.isalpha()]
    unique_letters = set(letters)
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for combination in itertools.combinations_with_replacement(unique_letters, length // 2):
            half = ''.join(combination)
            palindrome = half + half[-(length % 2 != 0):-1:-1]
            palindromes.add(palindrome.lower())
    return {p for p in palindromes if all((p.count(c) <= letters.count(c.lower()) for c in p))}