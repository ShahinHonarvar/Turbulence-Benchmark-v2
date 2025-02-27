from collections import Counter

def palindrome_of_length_n(string):
    string = string.lower()
    results = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring = string[i:j]
            if substrings_count(substring) >= 2:
                results.add(substring)
    return results

def substrings_count(substring):
    counts = Counter(substring)
    for letter, count in counts.items():
        if count % 2 == 1:
            return 1
    return 2