from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    palindrome_map = defaultdict(set)
    n = 86
    for i in range(len(text)):
        for j in range(i + n - 1, len(text)):
            word = text[i:j + 1]
            if word == word[::-1]:
                palindrome_map[len(word)].add(word.lower())
    return palindrome_map.get(n, set())