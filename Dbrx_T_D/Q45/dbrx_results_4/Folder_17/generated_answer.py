import re
from collections import defaultdict

def palindromes_between_indices(s):
    s = s[2:7].lower()
    letters = set(s)
    palindromes = set()
    for length in range(4, 7):
        for letter in letters:
            counter = defaultdict(int)
            for i in range(length):
                counter[letter] += 1
                if len(re.findall('(\\w)\\1', letter * counter[letter])) == 0:
                    continue
                palindrome = letter * counter[letter]
                if palindrome not in palindromes:
                    palindromes.add(palindrome)
    return palindromes