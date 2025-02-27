from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:10].lower()
    char_count = {}
    for char in substring:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    odd_count = sum((1 for count in char_count.values() if count % 2 != 0))
    if odd_count > 1:
        return set()
    mid = ''
    half = []
    for char, count in char_count.items():
        if count % 2 != 0:
            mid = char
        half.extend(char * (count // 2))
    half = ''.join(half)
    palindrome_set = set()
    for half_perm in set(permutations(half)):
        potential_palindrome = ''.join(half_perm)
        full_palindrome = potential_palindrome + mid + potential_palindrome[::-1]
        if len(full_palindrome) >= 3:
            palindrome_set.add(full_palindrome)
    return palindrome_set