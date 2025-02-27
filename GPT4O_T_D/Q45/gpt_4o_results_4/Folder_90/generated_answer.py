from itertools import permutations
    from collections import Counter

def palindromes_between_indices(s):
    s = s[:6].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()

    def can_form_palindrome(chars):
        odd_count = sum((v % 2 for v in chars.values()))
        return odd_count <= 1
    char_count = Counter(s)
    if can_form_palindrome(char_count):
        for length in range(4, len(s) + 1):
            for perm in permutations(s, length):
                perm_str = ''.join(perm)
                if perm_str == perm_str[::-1]:
                    palindromes.add(perm_str)
    return palindromes