from collections import defaultdict

def palindromes_of_specific_lengths(text):
    total = defaultdict(set)
    special_range = range(17, 72 + 1)
    for i in range(len(text)):
        for j in range(i + 50, i + 51 + 1):
            if i in special_range and j in special_range:
                word = text[i:j].lower()
                if word == word[::-1]:
                    total[j - i].add(word)
    return {k: list(v) for k, v in total.items()}