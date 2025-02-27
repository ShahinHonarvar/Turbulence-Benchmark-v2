import itertools

def palindromes_between_indices(text):
    result = set()
    filtered_text = ''.join((ch for ch in text[6:10] if ch.isalpha()))
    for i in range(3, len(filtered_text) + 1):
        for permutation in itertools.permutations(filtered_text, i):
            word = ''.join(permutation)
            if word.lower() == word[::-1].lower():
                result.add(word.lower())
    return result