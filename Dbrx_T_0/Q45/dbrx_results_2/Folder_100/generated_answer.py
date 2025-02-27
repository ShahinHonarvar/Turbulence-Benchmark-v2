from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(5):
        for j in range(i, 6):
            substring = s[i:j + 1].lower()
            if len(substring) < 6:
                continue
            chars = defaultdict(int)
            for char in substring:
                chars[char] += 1
            if all((count % 2 == 0 for count in chars.values())) or len(english_letters - set(chars.keys())) == 0:
                palindromes.add(''.join(sorted(chars.keys())))
    return palindromes