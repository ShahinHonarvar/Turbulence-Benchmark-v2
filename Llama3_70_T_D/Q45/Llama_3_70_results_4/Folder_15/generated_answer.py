def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:3] if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for p in __import__('itertools').combinations(letters, length):
            for last in letters:
                palindrome = ''.join(p) + last + ''.join(reversed(p))
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes