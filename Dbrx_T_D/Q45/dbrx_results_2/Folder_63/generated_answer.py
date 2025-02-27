from collections import defaultdict

def palindromes_between_indices(s):
    char_count = defaultdict(int)
    for char in s[:4].lower():
        if char.isalpha():
            char_count[char] += 1
    palindromes = set()
    for a in filter(char_count.get, string.ascii_lowercase):
        for b in filter(char_count.get, string.ascii_lowercase):
            if char_count[b] >= char_count[a]:
                palindromes.add(a + b + a)
    for length in range(5, min(char_count.values(), 5) + 1):
        for palindrome in palindromes.copy():
            for c in filter(char_count.get, string.ascii_lowercase):
                if char_count[c] >= 1:
                    palindromes.add(palindrome + c + palindrome[::-1])
    return palindromes