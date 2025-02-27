import re
    from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = set(re.findall('[a-zA-Z]', s[1:8]))
    palindromes = set()
    for length in range(3, len(english_letters) + 1):
        chars = defaultdict(int)
        for c in english_letters:
            chars[c] += 1
        for c in english_letters:
            if chars[c] > 1:
                palindromes.add(c * length)
            elif length % 2 == 0 and chars[c] >= 2:
                palindromes.add(c * (length - 1) + english_letters.pop())
            chars[c] -= 1
    return palindromes