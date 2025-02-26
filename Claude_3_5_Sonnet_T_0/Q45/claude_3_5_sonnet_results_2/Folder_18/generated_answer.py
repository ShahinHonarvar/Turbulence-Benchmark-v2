def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[1:7] if c.isalpha()))

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            for perm in generate_permutations(substring):
                if is_palindrome(perm):
                    palindromes.add(perm)
    return palindromes

def generate_permutations(s):
    if len(s) <= 1:
        yield s
    else:
        for i in range(len(s)):
            for perm in generate_permutations(s[:i] + s[i + 1:]):
                yield (s[i] + perm)