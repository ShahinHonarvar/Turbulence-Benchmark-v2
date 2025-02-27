import itertools

def palindromes_between_indices(s):

    def is_palindrome(string):
        return string == string[::-1]
    filtered_chars = [c for c in s[1:9] if c.isalpha()]
    filtered_chars = ''.join(filtered_chars).lower()
    palindromes = set()
    for length in range(7, len(filtered_chars) + 1):
        for combo in itertools.combinations(filtered_chars, length):
            candidate = ''.join(combo)
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes