import re
from collections import defaultdict

def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[28:95].lower()
    ascii_offset = 96
    letter_counts = defaultdict(int)
    for char in s:
        letter_counts[ord(char) - ascii_offset] += 1
    for length in range(38, 50):
        for i in range(len(s) - length + 1):
            count = {k: v for k, v in letter_counts.items() if k in range(ord('a') - ascii_offset, ord('z') - ascii_offset + 1)}
            for j in range(i, i + length):
                count[ord(s[j]) - ascii_offset] -= 1
                if count[ord(s[j]) - ascii_offset] < 0:
                    break
            else:
                if length % 2 == 0:
                    palindrome = s[i:i + length // 2] + s[i + length // 2 - 1:i + length // 2][::-1]
                else:
                    palindrome = s[i:i + length // 2] + s[i + length // 2][::-1]
                palindromes.add(palindrome)
    return palindromes