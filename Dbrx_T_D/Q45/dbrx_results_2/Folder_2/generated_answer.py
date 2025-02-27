from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = {chr(i) for i in range(ord('a'), ord('z') + 1)}.union({chr(i) for i in range(ord('A'), ord('Z') + 1)})
    substr = s[1:6]
    chars = {c for c in substr if c in english_letters}
    if len(chars) < 3:
        return set()

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for length in range(6, len(chars) + 1):
        for chars_combination in itertools.combinations(chars, length):
            combination = ''.join(chars_combination)
            if is_palindrome(combination):
                palindromes.add(combination.lower())
    return palindromes