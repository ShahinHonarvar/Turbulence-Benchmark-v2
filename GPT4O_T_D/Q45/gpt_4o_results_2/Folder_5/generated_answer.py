import itertools

def palindromes_between_indices(s):

    def is_palindrome(phrase):
        return phrase == phrase[::-1]
    s = s[4:9].lower()
    filtered_chars = [c for c in s if c.isalpha()]
    palindromes_set = set()
    for length in range(4, len(filtered_chars) + 1):
        for combo in itertools.permutations(filtered_chars, length):
            candidate = ''.join(combo)
            if is_palindrome(candidate):
                palindromes_set.add(candidate)
    return palindromes_set