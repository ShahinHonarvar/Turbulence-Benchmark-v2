from collections import defaultdict
from functools import partial

def palindrome_of_length_at_least_n(s):

    def character_counts(text):
        return reduce(lambda counts, c: counts.update({c.lower(): counts.get(c.lower(), 0) + 1}), text, defaultdict(int))
    all_palindromes = set()
    for word in s.split():
        word_counts = character_counts(word)
        for i in range(1, len(word) + 1):
            if 2 * i <= len(word):
                if all((count % 2 == 0 for count in word_counts.values())):
                    all_palindromes.add(word)
            for c in word_counts:
                if word_counts[c] >= 4 * i:
                    all_palindromes.add(word)
                if word_counts[c] >= 2 and word_counts[c] % 2 == 0:
                    if (word_counts[c] - 2) % 4 * i == 0:
                        all_palindromes.add(word)
    return all_palindromes