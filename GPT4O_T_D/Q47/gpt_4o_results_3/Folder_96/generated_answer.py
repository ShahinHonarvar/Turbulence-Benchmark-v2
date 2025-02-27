def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    subset = [c.lower() for c in s[100:301] if c.isalpha()]
    results = set()
    n = len(subset)
    for length in range(50, 101):
        for start in range(n - length + 1):
            candidate = ''.join(subset[start:start + length])
            if is_palindrome(candidate):
                results.add(candidate)
    return results