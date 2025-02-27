from collections import defaultdict

def if_contains_anagrams(str_list):
    count = defaultdict(int)
    for word in str_list:
        if len(word) >= 3:
            count[''.join(sorted(word.lower()))] += 1
    anagram_pairs = sum((n * (n - 1) // 2 for n in count.values()))
    return anagram_pairs <= 36