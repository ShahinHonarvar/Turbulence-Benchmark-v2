from collections import defaultdict

def palindromes_between_indices(s):
    result = set()
    for length in range(5, 9):
        chars = defaultdict(int)
        for i in range(8, 4 + length):
            chars[s.lower()[i]] += 1
        for word in map(''.join, chars.items()):
            if len(word) == len(set(word)) and word == word[::-1]:
                result.add(word)
    return result