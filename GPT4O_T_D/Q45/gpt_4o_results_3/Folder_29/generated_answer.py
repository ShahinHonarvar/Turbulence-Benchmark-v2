import itertools

def palindromes_between_indices(s):
    s = s.lower()
    sub_str = ''.join((c for c in s[2:10] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for length in range(6, len(sub_str) + 1):
        for combo in itertools.permutations(sub_str, length):
            word = ''.join(combo)
            if is_palindrome(word):
                palindromes.add(word)
    return palindromes