from collections import defaultdict

def is_palindrome(word):
    return word == word[::-1]

def build_suffix_tree(word):
    suffixes = defaultdict(list)
    for i in range(len(word)):
        suffix = word[i:]
        suffixes[suffix[0]].append(suffix)
    return suffixes

def palindrome_of_length_n(words, n):
    letters = ''.join(words).lower()
    suffix_tree = build_suffix_tree(letters)
    palindromes = set()
    for key in suffix_tree:
        for suffix in suffix_tree[key]:
            if len(suffix) >= n:
                palindrome = suffix[:n]
                if is_palindrome(palindrome):
                    palindromes.add(palindrome)
    return palindromes