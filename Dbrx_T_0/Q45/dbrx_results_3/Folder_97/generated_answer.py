from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(5):
        for j in range(i, 5):
            substring = s[i:j + 1].lower()
            if len(substring) < 3:
                continue
            chars = defaultdict(int)
            for char in substring:
                chars[char] += 1
            if all((count % 2 == 0 for count in chars.values())) or len(chars) == 1:
                palindromes.add(''.join(sorted(english_letters & set(substring))))
    return palindromes