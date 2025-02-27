from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindrome_multisets = defaultdict(set)
    for i in range(len(text) - 100 + 1):
        for j in range(i + 100, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                palindrome_multisets[j - i].add(substring)
    return set(palindrome_multisets.values())