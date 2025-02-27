import string
    import itertools
    from collections import Counter

def palindromes_between_indices(string_input):
    string_input = string_input.lower()
    letters = Counter(filter(lambda x: x in string.ascii_lowercase, string_input[2:10]))
    length = 4
    palindromes = set()
    while length <= len(string_input[2:10]):
        for p in itertools.permutations(letters.keys(), length):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
        length += 1
    return palindromes