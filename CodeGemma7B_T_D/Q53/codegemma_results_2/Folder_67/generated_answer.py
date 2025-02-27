from collections import defaultdict

def palindrome_of_length_at_least_n(string):
    char_counts = defaultdict(int)
    for char in string.lower():
        if char.isalpha():
            char_counts[char] += 1
    result = set()
    for char, count in char_counts.items():
        if count >= 25:
            result.add(char * count)
    return result