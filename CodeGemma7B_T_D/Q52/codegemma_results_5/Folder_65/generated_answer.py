from collections import defaultdict
import re

def palindrome_of_length_n(text):
    palindromes = defaultdict(set)
    for i in range(len(text)):
        for j in range(i + 5, len(text) + 1):
            subtext = text[i:j]
            if subtext == subtext[::-1] and subtext.isalpha():
                palindromes[len(subtext)].add(subtext)
    return set((values for values in palindromes.values() if len(values) > 0))