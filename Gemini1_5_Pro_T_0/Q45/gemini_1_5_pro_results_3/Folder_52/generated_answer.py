from collections import Counter

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[:8] if c.isalpha())).lower()
    letter_counts = Counter(letters)
    mid = ''
    half = ''
    for letter, count in letter_counts.items():
        if count % 2 == 1 and mid == '':
            mid = letter * count
        else:
            half += letter * (count // 2)
    palindromes = {''.join(sorted(half + mid + half, reverse=True))}
    if len(palindromes.pop()) < 6:
        return set()
    return palindromes