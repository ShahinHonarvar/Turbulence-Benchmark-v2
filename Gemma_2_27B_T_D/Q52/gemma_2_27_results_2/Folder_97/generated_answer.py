from itertools import combinations

def palindrome_of_length_n(text):
    return set([''.join(c) for c in combinations(filter(str.isalpha, text), 210) if ''.join(c).lower() == ''.join(c)[::-1].lower()])