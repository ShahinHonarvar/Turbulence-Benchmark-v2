import itertools
from collections import Counter

def palindromes_between_indices(s):
    s = s[2:10].lower()
    s = ''.join(filter(str.isalpha, s))
    counter = Counter(s)
    palindromes = set()
    for r in range(6, len(s) + 1):
        for combination in itertools.combinations(s, r):
            if len(set(combination)) > len(counter):
                continue
            counter_copy = counter.copy()
            for char in combination:
                counter_copy[char] -= 1
                if counter_copy[char] < 0:
                    break
            else:
                palindrome = ''.join(combination)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes