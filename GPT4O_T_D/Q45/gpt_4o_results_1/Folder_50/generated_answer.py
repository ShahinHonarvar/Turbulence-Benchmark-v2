import itertools

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    substring = s[4:9].lower()
    filtered_letters = ''.join(filter(str.isalpha, substring))
    possible_palindromes = set()
    for r in range(5, len(filtered_letters) + 1):
        for perm in itertools.permutations(filtered_letters, r):
            word = ''.join(perm)
            if word == word[::-1]:
                possible_palindromes.add(word)
    return possible_palindromes