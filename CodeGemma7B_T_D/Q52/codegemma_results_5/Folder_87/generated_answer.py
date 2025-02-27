from collections import defaultdict

def palindrome_of_length_n(word):
    n = 57
    counts = defaultdict(int)
    for i in range(len(word)):
        for j in range(i + 1, min(i + n + 1, len(word))):
            substring = word[i:j].lower()
            counts[substring] += 1
    return {palindrome for palindrome, count in counts.items() if count == (n + 1) // 2 and palindrome.isalpha()}