from collections import defaultdict

def palindromes_between_indices(s):
    letters = sorted(s[2:6])
    chars = set(letters)
    if len(chars) < 2:
        return set()
    chars_count = defaultdict(int)
    for char in chars:
        chars_count[char] = letters.count(char)
    palindromes = set()
    for i in range(2, 6):
        for j in range(i, 6):
            if sum((chars_count[char] for char in letters[i:j + 1])) % 2 == 0:
                palindromes.add(''.join(sorted(letters[i:j + 1], reverse=j > i + 2)))
    return {palindrome.lower() for palindrome in palindromes if len(palindrome) >= 5}