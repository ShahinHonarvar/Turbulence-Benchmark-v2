from collections import defaultdict
import re

def form_palindrome(char_freq, length):
    chars = [char for char, freq in char_freq.items() if freq % 2 == 1]
    odd_freq_chars = len(chars)
    if odd_freq_chars > length:
        return None
    chars.sort(key=lambda x: char_freq[x], reverse=True)
    chars.append(chars[-1])
    palindrome = []
    for i in range(length // 2 + 1):
        if i < odd_freq_chars:
            palindrome.append(chars[i])
        else:
            palindrome.append(chars[-i])
    return ''.join(palindrome)

def count_chars(string):
    char_freq = defaultdict(int)
    for char in string.lower():
        if char.isalpha():
            char_freq[char] += 1
    return char_freq

def palindromes_between_indices(string):
    if len(string) < 10:
        return set()
    char_freq = count_chars(string[2:10])
    palindromes = set()
    for length in range(4, 10):
        palindrome = form_palindrome(char_freq, length)
        if palindrome:
            palindromes.add(palindrome)
    return palindromes