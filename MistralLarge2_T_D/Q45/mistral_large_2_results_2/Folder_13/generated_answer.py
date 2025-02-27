from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    subset = s[3:10]
    letters = ''.join(filter(str.isalpha, subset)).lower()
    letter_count = Counter(letters)
    palindromes = set()
    for length in range(5, len(letters) + 1):
        if length % 2 == 0:
            half = length // 2
            for perm in permutations(letter_count.elements(), half):
                if all((letter_count[char] >= perm.count(char) for char in perm)):
                    palindrome = ''.join(perm) + ''.join(reversed(perm))
                    palindromes.add(palindrome)
        else:
            half = length // 2
            for center in letter_count:
                if letter_count[center] > 0:
                    remaining_count = letter_count.copy()
                    remaining_count[center] -= 1
                    for perm in permutations(remaining_count.elements(), half):
                        if all((remaining_count[char] >= perm.count(char) for char in perm)):
                            palindrome = ''.join(perm) + center + ''.join(reversed(perm))
                            palindromes.add(palindrome)
    return palindromes