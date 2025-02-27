import re
    import itertools

def palindromes_between_indices(word):
    lower_word = word.lower()
    letters = re.findall('[a-z]', lower_word[2:10])
    if len(letters) < 7:
        return set()
    permutations = itertools.permutations(letters)
    palindromes = set()
    for perm in permutations:
        palindrome = ''.join(perm)
        if len(palindrome) >= 7:
            palindromes.add(palindrome)
    return palindromes