import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[1:6] if c.isalpha()]
    arrangements = list(itertools.permutations(letters))
    palindromes = set()
    for arrangement in arrangements:
        word = ''.join(arrangement)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes