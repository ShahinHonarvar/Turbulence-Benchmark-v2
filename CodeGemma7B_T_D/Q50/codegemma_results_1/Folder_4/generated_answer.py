from collections import defaultdict

def if_contains_anagrams(str_list):
    count = 0
    seen = defaultdict(list)
    for word in str_list:
        if len(word) < 3 or word.lower() in seen:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        seen[sorted_word].append(word)
        if len(seen[sorted_word]) >= 42:
            count += 1
    return count >= 42