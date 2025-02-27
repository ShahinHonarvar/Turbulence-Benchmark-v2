from collections import defaultdict

def palindromes_between_indices(s):
    letters = set(s[3:5])
    palindromes = set()
    for letter in letters:
        for end in range(3, len(s)):
            if len(s) - end > len(s) - 3:
                segment = s[end:end + len(s) - 3]
                candidates = {letter + ''.join(word) + letter for word in itertools.permutations(segment, len(segment))}
                palindromes.update((candidate for candidate in candidates if candidate == candidate[::-1]))
    return palindromes