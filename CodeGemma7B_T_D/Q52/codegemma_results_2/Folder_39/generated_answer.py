from itertools import combinations

def palindrome_of_length_n(str1):
    str1 = str1.lower()
    return {substring for substring in str1 for L, R in combinations(range(len(substring)), 2) if substring[L] == substring[R] and R - L == 29}