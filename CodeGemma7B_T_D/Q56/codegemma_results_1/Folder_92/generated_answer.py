from itertools import product

def all_substring_of_size_n(str):
    subs = []
    for i in product(range(len(str) - 9 + 1), repeat=9):
        subs.append(''.join((str[i[j]:i[j] + 1] for j in range(9))))
    return list(set(subs))