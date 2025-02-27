from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substring = s[2:6]
    letter_counts = {}
    for char in substring:
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1

    def can_form_palindrome(perm):
        l = len(perm)
        for i in range(l // 2):
            if perm[i] != perm[l - i - 1]:
                return False
        return True
    unique_perms = set()
    for perm in permutations(substring):
        if can_form_palindrome(perm) and len(perm) >= 4:
            unique_perms.add(''.join(perm))
    return unique_perms