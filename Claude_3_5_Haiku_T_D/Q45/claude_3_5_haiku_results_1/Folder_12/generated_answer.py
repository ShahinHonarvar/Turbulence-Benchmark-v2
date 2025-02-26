from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:9] if c.isalpha()]
    palindromes = set()

    def can_form_palindrome(chars):
        char_count = {}
        for char in chars:
            char_count[char] = char_count.get(char, 0) + 1
        odd_count = sum((1 for count in char_count.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(chars):
        if not can_form_palindrome(chars):
            return set()
        unique_perms = set(permutations(chars))
        valid_palindromes = set()
        for perm in unique_perms:
            for mid in range(len(perm) // 2 + 1):
                left = list(perm[:mid])
                right = list(perm[mid:])
                if mid > 0:
                    mid_char = [perm[mid - 1]]
                else:
                    mid_char = []
                pal = left + mid_char + list(reversed(right))
                pal_str = ''.join(pal)
                if len(pal_str) >= 4 and pal_str == pal_str[::-1]:
                    valid_palindromes.add(pal_str)
        return valid_palindromes
    return generate_palindromes(letters)