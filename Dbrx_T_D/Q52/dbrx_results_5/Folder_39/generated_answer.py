from collections import defaultdict

def palindrome_of_length_n(s: str) -> set:

    def is_palindrome(s: str) -> bool:
        s = ''.join((c.lower() for c in s if c.isalpha()))
        return s == s[::-1]
    n = 59
    if len(s) < n:
        return set()
    palindromes = defaultdict(set)
    for i in range(len(s) - n + 1):
        for j in range(i, i + n):
            if is_palindrome(s[i:j + 1]):
                palindromes[i].add(s[i:j + 1])
    return {palindrome for start_index, palindromes_at_index in palindromes.items() for palindrome in palindromes_at_index}