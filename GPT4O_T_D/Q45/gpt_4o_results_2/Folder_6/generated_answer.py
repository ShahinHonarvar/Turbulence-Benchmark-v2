from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(perm):
        return perm == perm[::-1]

    def get_letter_counts(substring):
        counts = {}
        for char in substring:
            if char.isalpha():
                char = char.lower()
                counts[char] = counts.get(char, 0) + 1
        return counts
    substring = s[:8]
    letter_counts = get_letter_counts(substring)
    letters = ''.join((char * (count // 2 * 2) for char, count in letter_counts.items()))
    half_length = len(letters) // 2
    results = set()
    for perm in set(permutations(letters, half_length)):
        half = ''.join(perm)
        full = half + half[::-1]
        if len(full) >= 4:
            results.add(full)
    return results