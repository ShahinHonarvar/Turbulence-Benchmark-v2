from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    count = defaultdict(int)
    for i in range(len(text)):
        for j in range(i):
            count[text[j:i + 1]] += 1
    res = set()
    for key, value in count.items():
        if len(key) >= 33 and value >= 2:
            res.add(key)
    return res