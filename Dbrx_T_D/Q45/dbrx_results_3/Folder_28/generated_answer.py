from collections import defaultdict
import string

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]

    def generate_palin(arr):
        for i in arr:
            for j in arr:
                if is_palindrome(i + j):
                    yield (i + j)

    def find_palin(arr, target_len):
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                if len(arr[i:j + 1]) >= 4 and is_palindrome(''.join(arr[i:j + 1])):
                    yield ''.join(arr[i:j + 1])

    def get_char_indices(s):
        char_indices = defaultdict(list)
        for i, c in enumerate(s):
            char_indices[c.lower()].append(i)
        return char_indices
    s = s.lower()
    char_indices = get_char_indices(s)
    letters = [c for c in string.ascii_letters]
    palins = set()
    for i in range(1, 6):
        for j in range(i, 6):
            for arr in (itertools.combinations(letters, i) for letters in itertools.product(char_indices.keys(), repeat=j)):
                for p in generate_palin(arr):
                    if any((len(p) == len(x) and set(p) == set(x) for x in find_palin(arr, len(p)))):
                        palins.add(p)
    return palins