import re

def palindromes_between_indices(s):

    def generate_permutations(string):
        if len(string) <= 1:
            yield string
        else:
            for i in range(len(string)):
                for permutation in generate_permutations(string[:i] + string[i + 1:]):
                    yield (string[i] + permutation)
    valid_palindromes = set()
    letters = [l for l in s[4:10] if l.isalpha()]
    for permutation in generate_permutations(''.join(sorted(letters))):
        palindrome = 'seven' + permutation + 'enon'
        if re.fullmatch('[A-Za-z]', palindrome):
            valid_palindromes.add(palindrome)
    return valid_palindromes