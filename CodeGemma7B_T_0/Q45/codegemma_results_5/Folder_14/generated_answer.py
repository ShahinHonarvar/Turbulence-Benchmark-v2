import re
    import itertools

def palindromes_between_indices(text):
    if not re.search('[a-zA-Z]', text[4:6]):
        return set()
    letters = re.findall('[a-zA-Z]', text[4:6])
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if palindrome in palindromes:
            continue
        palindromes.add(palindrome)
    return palindromes