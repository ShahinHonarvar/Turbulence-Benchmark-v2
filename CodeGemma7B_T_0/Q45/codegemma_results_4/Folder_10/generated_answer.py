import re
    from itertools import permutations

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    if len(text) < 6:
        return set()
    palindromes = set()
    for i in range(len(text) - 5):
        for j in range(i + 3, len(text)):
            for permutation in permutations(text[i:j + 1]):
                palindrome = ''.join(permutation)
                if palindrome not in palindromes:
                    palindromes.add(palindrome)
    return palindromes