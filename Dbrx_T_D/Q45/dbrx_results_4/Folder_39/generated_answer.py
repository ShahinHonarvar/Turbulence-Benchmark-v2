from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = {chr(i).lower() for i in range(ord('a'), ord('z') + 1)}
    letters = defaultdict(int)
    for i in range(2, 6):
        if i < len(s) and s[i].lower() in english_letters:
            letters[s[i].lower()] += 1
    palindromes = set()
    for i in range(len(letters)):
        for letter, count in letters.items():
            if count - i >= i:
                palindromes.add((''.join(letter * (i * 2 + 1)) for _ in range(count - i)))
    return palindromes