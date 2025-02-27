import itertools

def palindromes_between_indices(s):
    palindromes = set()
    letters = [c.lower() for c in s[:8] if c.isalpha()]
    if len(set(letters)) < 7:
        return palindromes
    arrangements = list(itertools.permutations(letters))
    for arrangement in arrangements:
        possible_palindrome = ''.join(arrangement)
        if len(possible_palindrome) >= 7:
            palindromes.add(possible_palindrome)
    return palindromes