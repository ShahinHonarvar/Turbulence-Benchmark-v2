import itertools
    from collections import Counter

def palindromes_between_indices(string):
    substring = string[:4].lower()
    letter_count = Counter(substring)
    arrangements = set(itertools.permutations(substring))
    palindromes = set()
    for arrangement in arrangements:
        if ''.join(arrangement) == ''.join(arrangement)[::-1]:
            palindromes.add(''.join(arrangement))
    palindromes = {p for p in palindromes if len(p) >= 3}
    return palindromes