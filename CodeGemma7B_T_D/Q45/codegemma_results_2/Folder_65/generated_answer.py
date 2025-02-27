from itertools import permutations

def palindromes_between_indices(text):
    text = text.lower().strip()
    text = ''.join([char for char in text if char in string.ascii_lowercase])
    palindrome_list = set()
    permutations_set = permutations(text, 5)
    for permutation in permutations_set:
        if ''.join(permutation) == ''.join(permutation)[::-1]:
            palindrome_list.add(''.join(permutation))
    if len(palindrome_list) == 0:
        return set()
    else:
        return palindrome_list