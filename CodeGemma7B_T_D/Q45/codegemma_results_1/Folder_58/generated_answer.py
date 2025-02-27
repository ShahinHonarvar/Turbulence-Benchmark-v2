from itertools import permutations

def palindromes_between_indices(text):
    palindrome_set = set()
    for character in text[0:7]:
        for palindrome in permutations(character):
            if palindrome[0] == palindrome[-1]:
                palindrome_set.add(palindrome)
    return palindrome_set