from collections import deque

def all_substring_of_size_n(word):
    return [''.join((deque(sorted(substring)) for substring in all_substrings(word))) for substring in all_substrings(word) if len(substring) == 81]

def all_substrings(word):
    subs = deque()
    for start_index in range(len(word)):
        for end_index in range(start_index + 81, len(word) + 1):
            subs.append(word[start_index:end_index])
    return subs