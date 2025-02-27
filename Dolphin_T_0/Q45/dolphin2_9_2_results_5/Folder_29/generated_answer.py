import itertools

def palindromes_between_indices(s):
    sub_s = s[2:10]
    characters = [char.lower() for char in sub_s if char.isalpha()]
    palindromes = set()
    for i in range(6, len(characters) + 1):
        for combo in itertools.permutations(characters, i):
            word = ''.join(combo)
            if word.lower() == word[::-1].lower():
                palindromes.add(''.join(combo))
    return palindromes