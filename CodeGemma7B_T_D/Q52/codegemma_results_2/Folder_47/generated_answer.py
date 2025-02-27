import re
from itertools import product

def palindrome_of_length_n(string):
    pattern = '[a-zA-Z]{34}'
    if not re.findall(pattern, string):
        return set()

    def generate_combinations(length):
        letters = list(string.lower())
        combinations = list(product(repeat=letters, times=length))
        return combinations
    combinations = generate_combinations(34)
    palindromes = set()
    for combination in combinations:
        palindrome = ''.join(combination)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes