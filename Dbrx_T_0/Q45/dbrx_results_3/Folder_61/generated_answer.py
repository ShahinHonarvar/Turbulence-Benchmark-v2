from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(0, 8):
        for j in range(i, 8):
            substring = s[i:j + 1].lower()
            if len(substring) < 7:
                continue
            chars = defaultdict(int)
            for char in substring:
                chars[char] += 1
            if all((count % 2 == 0 for count in chars.values())) or (len(substring) % 2 == 1 and all(((count - 1) % 2 == 0 for count in chars.values()))):
                palindromes.add(''.join((char * (count // 2) for char, count in chars.items())) + substring[len(substring) // 2] * (len(substring) % 2))
    return palindromes