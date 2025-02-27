from itertools import permutations

def palindromes_between_indices(word):
    word = word.casefold()
    letters = [c for c in word[2:7]]
    palindromes = set()
    for p in permutations(letters):
        palindrome = ''.join(p)
        if len(palindrome) >= 5 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes