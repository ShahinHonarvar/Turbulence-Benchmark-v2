from itertools import permutations

def palindromes_between_indices(s):
    sub_s = ''.join(sorted(s[0:6].lower()))
    palindrome_set = set()
    for p in permutations(sub_s):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 6:
            palindrome_set.add(word)
    return palindrome_set