from collections import defaultdict

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindrome_set = set()
    count = defaultdict(int)
    n = 141
    for c in s:
        count[c] += 1
    for char in count:
        if count[char] >= n and char.isalpha():
            palindrome_set.add(char * count[char])
    return palindrome_set