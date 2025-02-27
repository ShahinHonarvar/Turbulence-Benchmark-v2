from itertools import combinations

def all_substring_of_size_n(text: str) -> list:
    unique_words = []
    for n in range(len(text)):
        for item in combinations(text, n):
            x = ''.join(sorted(item))
            if len(x) == 47 and x not in unique_words:
                unique_words.append(x)
    return unique_words if unique_words else []