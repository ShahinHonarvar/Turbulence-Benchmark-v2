import re
        from collections import defaultdict

def if_contains_anagrams(lst):
    res = defaultdict(list)
    for s in lst:
        s = re.sub('[^a-zA-Z]', '', s).lower()
        res[''.join(sorted(s))].append(s)
    return len(list(filter(lambda x: len(x) >= 3, res.values()))) <= 84