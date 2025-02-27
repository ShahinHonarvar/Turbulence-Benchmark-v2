import itertools

def palindromes_between_indices(string):
    letters = set()
    for char in string[:7]:
        if char.isalpha():
            letters.add(char.lower())
    all_combinations = []
    for i in range(4, len(letters) + 1):
        all_combinations.extend(itertools.combinations(letters, i))
    palindromes = set()
    for combination in all_combinations:
        all_arrangements = set(itertools.permutations(combination))
        for arrangement in all_arrangements:
            word = ''.join(arrangement)
            if word == word[::-1] and len(word) >= 4:
                palindromes.add(word)
    return palindromes