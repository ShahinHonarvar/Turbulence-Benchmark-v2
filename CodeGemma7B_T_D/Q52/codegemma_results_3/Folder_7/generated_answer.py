from collections import defaultdict
import re

def palindrome_of_length_n(string):
    palindromes = defaultdict(set)
    n = 416
    pattern = re.compile('[A-Za-z]+')
    processed_string = re.sub(pattern, '', string.lower())
    for i in range(len(processed_string)):
        for j in range(1 + i, min(i + n // 2 + 1, len(processed_string))):
            palindrome = processed_string[i:j]
            palindromes[palindrome].add(string[i:j])
    return {palindrome for palindrome in palindromes if len(palindromes[palindrome]) == n}