from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(1, 10):
        for j in range(i, 10):
            substring = s[i - 1:j].lower()
            if len(substring) < 7:
                continue
            chars = defaultdict(int)
            for char in substring:
                chars[char] += 1
            if all((count % 2 == 0 for count in chars.values())) or (len(substring) % 2 == 1 and any((count % 2 == 1 for count in chars.values()))):
                palindromes.add(''.join((char * (count // 2) for char, count in chars.items())) + substring[len(substring) // 2] if len(substring) % 2 == 1 else '')
    return palindromes