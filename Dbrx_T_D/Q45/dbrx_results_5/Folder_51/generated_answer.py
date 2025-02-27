from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = {c.lower() for c in s if c.lower() in 'abcdefghijklmnopqrstuvwxyz'}
    if len(english_letters) == 0 or len(s) < 6:
        return set()
    palindromes = set()
    for length in range(3, len(english_letters) + 1):
        substr = s[3:6]
        substr = ''.join((c for c in substr if c.lower() in english_letters))
        if len(substr) < length:
            continue
        chars = defaultdict(int)
        for c in substr:
            chars[c] += 1
        odd_count = sum((1 for c in chars.values() if c % 2 != 0))
        if odd_count > 1:
            continue
        if length % 2 == 0:
            pairs = [(k, v // 2) for k, v in chars.items() if v % 2 == 0]
            palindrome = ''.join((k * v for k, v in pairs))
        else:
            odd_char = next((k for k, v in chars.items() if v % 2 != 0), None)
            if odd_char is None:
                palindrome = ''.join((k * (v // 2) for k, v in chars.items()))
            else:
                pairs = [(k, v // 2) for k, v in chars.items() if k != odd_char]
                palindrome = odd_char + ''.join((k * v for k, v in pairs))
        palindromes.add(palindrome)
    return palindromes