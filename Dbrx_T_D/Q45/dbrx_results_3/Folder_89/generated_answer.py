from collections import defaultdict

def palindromes_between_indices(s):
    palindromes = set()
    string_indices = list(range(5, 10))
    substr = s[5:10].lower()
    chars = defaultdict(int)
    for char in substr:
        chars[char] += 1
    for length in range(6, len(substr) + 1):
        for i in string_indices:
            if i + length > len(substr) or i + length - 1 > len(substr):
                break
            permutation = ''.join((chars[char] for char in substr[i:i + length]))
            if is_palindrome(permutation):
                palindromes.add(permutation)
    return palindromes

def is_palindrome(s):
    return s == s[::-1]