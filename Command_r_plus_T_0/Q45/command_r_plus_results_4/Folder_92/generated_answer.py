def palindromes_between_indices(s):
    sub_str = s[4:8].lower()
    english_letters = ''.join(filter(str.isalpha, sub_str))
    arrangements = set(itertools.permutations(english_letters, len(english_letters)))
    palindromes = set((arrangement for arrangement in arrangements if len(arrangement) >= 4 and arrangement == arrangement[::-1]))
    return palindromes