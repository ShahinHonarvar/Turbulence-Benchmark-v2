import itertools

def palindromes_between_indices(text):
    text = ''.join((ch for ch in text if ch.isalpha()))
    text = text.lower()
    if not text or len(text) < 9:
        return set()
    palindromes = set()
    for indices in itertools.combinations(range(9), size=3):
        substring = ''.join((text[i] for i in indices))
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes