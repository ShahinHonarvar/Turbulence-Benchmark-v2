from itertools import permutations
    from collections import defaultdict

def palindromes_between_indices(word):
    char_counts = defaultdict(int)
    for char in word[2:4]:
        char_counts[char.lower()] += 1
    if len(char_counts) < 3:
        return set()
    arrangements = permutations(char_counts.keys())
    palindromes = set()
    for arrangement in arrangements:
        palindrome = ''.join(arrangement)
        palindromes.add(palindrome)
    return palindromes