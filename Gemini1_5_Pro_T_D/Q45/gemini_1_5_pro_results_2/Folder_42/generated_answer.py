import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(re.sub('[^a-zA-Z]+', '', string[6:10]).lower()))
    palindrome_set = set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                palindrome_set.add(candidate)
    return palindrome_set