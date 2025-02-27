from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = frozenset('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    s = s[1:5]
    chars = defaultdict(int)
    for char in s:
        if char in english_letters:
            chars[char] += 1
    palindromes = set()
    for length in range(3, len(s) + 1):
        for combo in itertools.product(english_letters, repeat=length):
            if all((chars[char] >= combo.count(char) for char in english_letters)):
                palindrome = ''.join(combo)
                if s.startswith(palindrome[1:-1], palindrome[0].lower()) or s.startswith(palindrome[1:-1], palindrome[0].upper()):
                    palindromes.add(palindrome)
    return palindromes