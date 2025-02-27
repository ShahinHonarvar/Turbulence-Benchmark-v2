import itertools
    from string import ascii_letters

def palindromes_between_indices(s):
    english_letters = set(ascii_letters)
    substring = s[0:6]
    palindromes = set()
    for length in range(4, 7):
        for subset in itertools.combinations(substring, length):
            subset_set = set(subset)
            if subset_set.issubset(english_letters):
                subset_str = ''.join(subset).lower()
                reversed_str = subset_str[::-1]
                if subset_str == reversed_str:
                    palindromes.add(subset_str)
    return palindromes