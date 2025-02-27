import itertools
    import re

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string[1:5])
    arrangements = list(itertools.permutations(letters))
    palindromes = set()
    for arrangement in arrangements:
        word = ''.join(arrangement).lower()
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes