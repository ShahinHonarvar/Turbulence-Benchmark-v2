from collections import Counter
            from itertools import permutations

def palindromes_between_indices(string):
    if not string or len(string) < 6:
        return set()
    counter = Counter(string[3:9].lower())
    letters = list(counter.keys())
    if not letters or len(letters) < 3:
        return set()
    palindromes = set()
    for permutation in permutations(letters, len(letters)):
        palindrome = ''.join(permutation)
        if counter[palindrome[0]] >= palindrome.count(palindrome[0]):
            palindromes.add(palindrome)
    return palindromes