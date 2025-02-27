def return_vowels(vowels):
    if vowels[1] > 'F' and vowels[1] <= 'j':
        return list(itertools.filterfalse(lambda x: x not in ['a', 'e', 'i', 'o', 'u'], vowels[1:7]))
    else:
        return []