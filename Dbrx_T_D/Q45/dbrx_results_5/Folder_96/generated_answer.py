import re
    from collections import defaultdict

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:9] if c.isalpha()]
    char_count = defaultdict(int)
    for char in letters:
        char_count[char] += 1
    odd_count_chars = [char for char, count in char_count.items() if count % 2 != 0]
    if len(odd_count_chars) > 1:
        return set()
    palindromes = set()
    for char, count in char_count.items():
        palindrome = char * (count // 2) if char not in odd_count_chars else char + char * ((count - 1) // 2)
        palindromes.add(palindrome)
    palindromes = {palindrome for palindrome in palindromes if len(palindrome) >= 6}
    return palindromes