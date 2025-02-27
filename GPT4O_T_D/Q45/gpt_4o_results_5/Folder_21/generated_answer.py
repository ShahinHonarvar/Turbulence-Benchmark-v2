from itertools import permutations as iter_permutations

def palindromes_between_indices(s):
    allowed_chars = s[1:9].lower()
    filtered_chars = [c for c in allowed_chars if c.isalpha()]
    char_count = {}
    for char in filtered_chars:
        char_count[char] = char_count.get(char, 0) + 1
    odd_count_chars = {char for char, count in char_count.items() if count % 2 != 0}
    if len(filtered_chars) < 7 or len(odd_count_chars) > 1:
        return set()
    permutations = set()

    def generate_palindromes(half_permutation):
        full_length = len(half_permutation) * 2 + len(odd_count_chars)
        if full_length < 7:
            return
        odd_char = next(iter(odd_count_chars), '')
        first_half = ''.join(half_permutation)
        second_half = first_half[::-1]
        palindrome = first_half + odd_char + second_half
        if len(palindrome) >= 7:
            permutations.add(palindrome)
    half_length = (len(filtered_chars) - len(odd_count_chars)) // 2
    half_permutations = iter_permutations(''.join((char * (count // 2) for char, count in char_count.items())), half_length)
    for half_permutation in half_permutations:
        generate_palindromes(half_permutation)
    return permutations