from itertools import permutations

def palindromes_between_indices(s):
    sub_string = s[2:6]
    palindromes = {''.join(p) for p in set(permutations(sub_string, len(sub_string))) if len(set(p)) >= 3}
    palindrome_set = set()
    for word in palindromes:
        word = word.lower()
        if word == word[::-1]:
            palindrome_set.add(word)
    return palindrome_set