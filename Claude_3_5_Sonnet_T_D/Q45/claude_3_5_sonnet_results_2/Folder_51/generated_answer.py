def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:6] if c.isalpha()]

    def generate_palindromes(chars, current='', used=None):
        if used is None:
            used = [False] * len(chars)
        if len(current) >= 3:
            yield current
        for i in range(len(chars)):
            if not used[i]:
                used[i] = True
                yield from generate_palindromes(chars, chars[i] + current + chars[i], used)
                used[i] = False
    palindromes = set()
    for palindrome in generate_palindromes(letters):
        if len(palindrome) >= 3:
            palindromes.add(palindrome)
    return palindromes