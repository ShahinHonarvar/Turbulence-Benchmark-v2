import re
    from itertools import permutations

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    letters = text[0:9]
    palindromes = set()
    for permutation in permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes