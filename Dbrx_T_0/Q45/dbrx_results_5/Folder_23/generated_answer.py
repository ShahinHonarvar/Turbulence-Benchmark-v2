from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(7):
        for j in range(i, 7):
            substring = s[i:j + 1].lower()
            if len(substring) < 4:
                continue
            chars = defaultdict(int)
            for char in substring:
                chars[char] += 1
            if all((count % 2 == 0 for count in chars.values())) or (len(substring) % 2 == 1 and any((count % 2 == 1 for count in chars.values()))):
                palindromes.add(''.join((char * (count // 2) for char, count in chars.items())) + substring[len(substring) // 2] if len(substring) % 2 == 1 else '')
    return palindromes