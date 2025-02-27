import itertools
    from string import ascii_lowercase as lowercase

def palindromes_between_indices(text):
    text = text.lower()
    result = set()
    for permutation in itertools.permutations(lowercase):
        substring = text[5:10]
        if substring.lower() == ''.join(permutation):
            result.add(''.join(permutation))
    return result