from itertools import permutations

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[:3] if char.isalpha()]

    def can_form_palindrome(chars):
        char_counts = {}
        for char in chars:
            char_counts[char] = char_counts.get(char, 0) + 1
        odd_count = sum((1 for count in char_counts.values() if count % 2 != 0))
        return odd_count <= 1

    def generate_palindromes(chars):
        unique_perms = set(permutations(chars))
        palindrome_set = set()
        for perm in unique_perms:
            for length in range(3, len(perm) + 1):
                for start in range(len(perm) - length + 1):
                    subset = perm[start:start + length]
                    if can_form_palindrome(subset):
                        chars_list = list(subset)
                        if len(chars_list) % 2 == 1:
                            mid = len(chars_list) // 2
                            mid_char = chars_list[mid]
                            left = chars_list[:mid]
                            right = chars_list[mid + 1:]
                        else:
                            mid = len(chars_list) // 2
                            left = chars_list[:mid]
                            right = chars_list[mid:]
                        palindrome = ''.join(left + ([mid_char] if len(chars_list) % 2 == 1 else []) + list(reversed(right)))
                        if len(palindrome) >= 3:
                            palindrome_set.add(palindrome)
        return palindrome_set
    return generate_palindromes(letters)