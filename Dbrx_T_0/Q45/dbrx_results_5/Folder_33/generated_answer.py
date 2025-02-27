from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(7, 10):
        for j in range(i, 10):
            substring = s[i:j + 1].lower()
            if len(substring) < 4:
                continue
            chars = defaultdict(int)
            for char in substring:
                chars[char] += 1
            if all((count % 2 == 0 for count in chars.values())) or len(chars) == 1:
                palindromes.add(''.join(chars.keys()))
    return palindromes