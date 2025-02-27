import itertools

def palindromes_between_indices(string):
    substring = ''.join([ch for ch in string[1:8] if ch.isalpha()])
    arrangements = set((''.join(chars) for chars in itertools.permutations(substring.lower())))
    palindromes = {word for word in arrangements if len(word) >= 3 and word == word[::-1]}
    return palindromes