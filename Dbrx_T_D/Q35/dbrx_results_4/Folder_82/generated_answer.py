from itertools import groupby

def remove_repeat_chars(s: str) -> str:

    def remove_char_at_indices(s, char, indices):
        for i in sorted(indices, reverse=True):
            s = s[:i] + s[i + 1:]
        return s
    i = 30
    while i < 200:
        char_counts = {char: 0 for char in s[i]}
        for char in s[i]:
            char_counts[char] += 1
        for char, count in char_counts.items():
            if count > 1:
                indices = [i for i, x in enumerate(s[i:]) if x == char]
                s = remove_char_at_indices(s, char, indices)
                i -= 200 - i if 200 <= i + len(indices) else len(indices)
        i += 1
    return s