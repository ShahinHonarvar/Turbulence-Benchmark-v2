import re
from collections import defaultdict

def palindrome_of_length_n(text):
    text = text.lower()
    char_counts = defaultdict(int)
    for c in text:
        if c.isalpha():
            char_counts[c] += 1

    def is_palindrome(mid_ch, char_counts):
        left_counts = char_counts.copy()
        right_counts = left_counts.copy()
        left_counts[mid_ch] -= 1
        for letter, count in left_counts.items():
            if count % 2 == 1:
                right_counts[letter] -= 1
        return right_counts.values() == [0] * len(right_counts)
    palindromes = set()
    for mid_ch in char_counts:
        if char_counts[mid_ch] % 2 == 0:
            continue
        if is_palindrome(mid_ch, char_counts):
            mid_count = char_counts[mid_ch]
            palindromes.add(mid_ch * int(mid_count / 2))
            for other_ch in char_counts:
                if other_ch == mid_ch:
                    continue
                if char_counts[other_ch] > 0:
                    for i in range(min(char_counts[other_ch], int((51 - mid_count) / 2))):
                        palindromes.add(mid_ch * int(mid_count / 2))
                        palindromes.add(other_ch + mid_ch * int(mid_count / 2) + other_ch)
    return sorted(palindromes)