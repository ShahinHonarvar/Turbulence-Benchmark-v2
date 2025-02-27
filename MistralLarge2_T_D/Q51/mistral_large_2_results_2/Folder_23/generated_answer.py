from collections import defaultdict

def if_contains_anagrams(lst):
    count = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            count[''.join(sorted(word.lower()))] += 1
    return sum((count[key] * (count[key] - 1) // 2 for key in count)) <= 49