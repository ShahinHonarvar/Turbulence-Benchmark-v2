import itertools

def palindromes_between_indices(s):
    sub_string = s[5:9]
    char_set = set(sub_string)
    combinations = list(itertools.product(char_set, repeat=5))
    combinations += [x for x in itertools.product(char_set, repeat=6)]
    combinations += [x for x in itertools.product(char_set, repeat=7)]
    combinations += [x for x in itertools.product(char_set, repeat=8)]
    combinations += [x for x in itertools.product(char_set, repeat=9)]
    combinations += [x for x in itertools.product(char_set, repeat=10) if len(set(x)) == 1]
    palindromes = set()
    for combination in combinations:
        word = ''.join(combination)
        if word == word[::-1]:
            palindromes.add(word.lower())
    return palindromes