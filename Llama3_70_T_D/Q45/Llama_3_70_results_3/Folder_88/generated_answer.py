from itertools import permutations, combinations_with_replacement
import string

def palindromes_between_indices(s):
    s = s[3:8]
    s = ''.join(filter(str.isalpha, s)).lower()
    letters = sorted(set(s))
    result = set()
    for length in range(6, len(s) + 1):
        for combo in combinations_with_replacement(letters, length // 2):
            first_half = ''.join(combo)
            second_half = first_half[::-1]
            if length % 2 == 1:
                for middle in letters:
                    palindrome = first_half + middle + second_half
                    result.add(palindrome)
            else:
                palindrome = first_half + second_half
                result.add(palindrome)
    return result