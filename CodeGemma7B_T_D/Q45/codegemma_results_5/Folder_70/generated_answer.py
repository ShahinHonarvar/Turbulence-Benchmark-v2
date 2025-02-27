import itertools

def palindromes_between_indices(text):
    text_lower = text.lower()
    if not text_lower[1:7]:
        return set()
    unique_letters = set(text_lower[1:7])
    combinations = itertools.permutations(unique_letters, r=len(unique_letters))
    palindromes = set()
    for combination in combinations:
        palindrome = ''.join(combination)
        if palindrome in text_lower[1:7]:
            palindromes.add(palindrome)
    return palindromes