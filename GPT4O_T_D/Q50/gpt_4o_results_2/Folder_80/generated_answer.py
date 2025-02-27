from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    sorted_words = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_word = ''.join(sorted(s.lower()))
            sorted_words[sorted_word].append(s)
    for group in sorted_words.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
        if count >= 19:
            return True
    return False