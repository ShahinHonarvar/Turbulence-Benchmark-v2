from collections import Counter
  from string import ascii_lowercase
  from itertools import combinations

def palindrome_of_length_at_least_n(text):
    text = ''.join([ch.lower() for ch in text if ch in ascii_lowercase])
    palindrome = []
    for i in range(78, len(text)):
        for j in combinations(text, i):
            if j == j[::-1]:
                palindrome.append(j)
    return set(palindrome)