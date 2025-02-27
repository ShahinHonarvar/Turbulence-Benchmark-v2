from collections import defaultdict

def is_palindrome(substring):
    return all((substring[i] == substring[-i - 1] for i in range(len(substring) // 2)))

def find_palindromes(s):
    palindrome_indices = defaultdict(set)
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            if len(substring) > 1 and is_palindrome(substring):
                palindrome_indices[len(substring)].add(j)
    return palindrome_indices

def palindrome_of_length_n(s, n=51):
    if not isinstance(s, str):
        raise TypeError('Argument must be a string')
    if not all((c.isalpha() for c in s)):
        raise ValueError('String must contain only English letters')
    palindrome_indices = find_palindromes(s.lower())
    return {''.join(s[i:j + 1]).lower() for i, j in palindrome_indices[n]}