import itertools

def palindromes_between_indices(s):
    index_1 = 1
    index_2 = 8
    s = s[index_1:index_2 + 1]
    palindromes = set()
    for i in range(7, len(s) + 1):
        for c in itertools.combinations(s, i):
            word = ''.join(c)
            if word.lower() == word[::-1].lower():
                palindromes.add(word)
    return palindromes