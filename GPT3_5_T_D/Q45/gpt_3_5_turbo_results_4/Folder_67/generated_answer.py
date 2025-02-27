import itertools

def palindromes_between_indices(string):
    letters = string[2:7]
    arrangements = list(itertools.permutations(letters.upper()))
    palindromes = set()
    for arrangement in arrangements:
        word = ''.join(arrangement)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes