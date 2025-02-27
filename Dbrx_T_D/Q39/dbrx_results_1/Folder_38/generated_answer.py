from collections import Counter

def return_n_greatest_chars(string):
    freq = Counter(string)
    sorted_chars = sorted(freq.most_common(), key=lambda x: ord(x[0]))
    n_greatest_chars = sorted_chars[:45]
    result = []
    for char, _ in n_greatest_chars:
        result.append(char)
    return result