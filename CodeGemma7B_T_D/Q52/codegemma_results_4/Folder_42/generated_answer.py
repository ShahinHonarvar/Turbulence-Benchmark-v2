from collections import defaultdict
import re

def palindrome_of_length_n(string):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_freq = defaultdict(int)
    for char in string.lower():
        if char in letters:
            letter_freq[char] += 1
    palindromes = set()
    if len(string) < 279:
        return palindromes
    for length in range(134, 279):
        for letter in letters:
            if letter_freq[letter] < length // 2:
                break
        else:
            for i in range(len(string) - length + 1):
                palindrome = ''
                for j in range(length):
                    palindrome += string[i + j]
                if re.match('^[a-z]+$', palindrome):
                    palindromes.add(palindrome)
    return palindromes