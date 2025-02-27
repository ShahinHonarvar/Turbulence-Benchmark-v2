from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]

    def can_form_palindrome(counts):
        odd_count = sum((1 for count in counts.values() if count % 2 == 1))
        return odd_count <= 1
    sub = s[:7].lower()
    letter_counts = Counter(filter(str.isalpha, sub))
    result = set()
    if can_form_palindrome(letter_counts):
        for length in range(3, sum(letter_counts.values()) + 1):
            for perm in set(permutations(sub, length)):
                candidate = ''.join(perm)
                if is_palindrome(candidate):
                    result.add(candidate)
    return result