from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[:4] if char.isalpha()]
    palindrome_set = set()
    for perm in set(permutations(letters, len(letters))):
        for length in range(4, len(letters) + 1):
            if length % 2 == 0:
                half_length = length // 2
                left_half = perm[:half_length]
                right_half = list(reversed(left_half))
                candidate = list(left_half) + list(right_half)
                palindrome = ''.join(candidate)
                if len(set(palindrome)) > 1:
                    palindrome_set.add(palindrome)
            elif length % 2 == 1:
                mid_index = length // 2
                left_half = perm[:mid_index]
                mid_char = perm[mid_index]
                right_half = list(reversed(left_half))
                candidate = list(left_half) + [mid_char] + list(right_half)
                palindrome = ''.join(candidate)
                if len(set(palindrome)) > 1:
                    palindrome_set.add(palindrome)
    return palindrome_set