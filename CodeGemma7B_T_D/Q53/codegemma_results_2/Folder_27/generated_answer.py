from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    results = set()
    text = text.lower()
    for i in range(len(text)):
        for j in range(i + 1, len(text) + 1):
            word = text[i:j]
            if word in seen[len(word)]:
                results.add(word)
            seen[len(word)].add(word)
    return results