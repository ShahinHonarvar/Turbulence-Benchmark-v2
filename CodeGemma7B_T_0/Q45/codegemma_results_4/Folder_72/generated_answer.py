import re
    import itertools

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    letters = text[1:8]
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes