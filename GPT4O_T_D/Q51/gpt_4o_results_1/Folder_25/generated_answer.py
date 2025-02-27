from collections import defaultdict

def if_contains_anagrams(words):
    word_dict = defaultdict(list)
    for word in words:
        lw = word.lower()
        if len(lw) >= 3:
            key = ''.join(sorted(lw))
            word_dict[key].append(lw)
    pair_count = 0
    for key in word_dict:
        n = len(word_dict[key])
        if n > 1:
            pair_count += n * (n - 1) // 2
        if pair_count > 67:
            return False
    return True