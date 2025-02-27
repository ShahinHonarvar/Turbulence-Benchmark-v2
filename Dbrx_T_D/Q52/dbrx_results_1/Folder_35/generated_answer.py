import re

def palindrome_of_length_n(string, n=116):
    if n % 2 == 1:
        return set()
    string = string.lower()
    distinct_chars = set(string)
    if len(distinct_chars) < n // 2:
        return set()
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if len(substring) == n and all((c == substring[0] for c in substring)):
            palindromes.add(substring)
            continue
        first_half, second_half = (substring[:n // 2], substring[n // 2:][::-1])
        if first_half == second_half and all((c in distinct_chars for c in first_half)):
            palindromes.add(substring)
    return palindromes