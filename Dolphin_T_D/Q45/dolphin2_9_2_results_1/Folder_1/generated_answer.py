import itertools
    from string import ascii_letters

def palindromes_between_indices(s):
    sub_str = s[4:8]
    sub_str = ''.join(filter(lambda x: x in ascii_letters, sub_str))
    permutations = [''.join(p) for p in itertools.permutations(sub_str) if len(set(p)) == len(p)]
    palindromes = set()
    for word in permutations:
        if len(word) >= 5:
            palindromes.add(word)
    return palindromes