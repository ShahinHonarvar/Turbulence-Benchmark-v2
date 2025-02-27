from itertools import permutations
	import string

def palindromes_between_indices(s):
    palindrome_set = set()
    sub_string = s[4:9]
    for p in permutations(sub_string, 5):
        word = ''.join(p)
        if word.lower() == word.lower()[::-1] and all((c in string.ascii_letters for c in word)):
            palindrome_set.add(word)
    return palindrome_set