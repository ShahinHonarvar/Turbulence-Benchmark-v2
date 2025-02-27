from collections import defaultdict
    import re

def palindrome_of_length_n(x):
    d = defaultdict(list)
    pattern = re.compile('[a-zA-Z]+')
    x = x.lower()
    for i in range(len(x) - 80 + 1):
        sub_str = x[i:i + 80]
        if pattern.fullmatch(sub_str):
            d[sub_str].append(sub_str)
    return d