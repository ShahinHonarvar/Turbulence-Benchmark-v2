from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(6, 10):
        for j in range(i, 10):
            substring = s[i:j + 1].lower()
            if len(substring) < 5:
                continue
            chars = defaultdict(int)
            for char in substring:
                if char in english_letters:
                    chars[char] += 1
            if all((count % 2 == 0 for count in chars.values())):
                palindromes.add(''.join((char * (count // 2) for char, count in chars.items())))
            elif len(chars) == 1:
                palindromes.add(''.join(chars.keys()))
    return palindromes