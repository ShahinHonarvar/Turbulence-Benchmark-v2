import collections

def if_contains_anagrams(string_list):
    anagrams = collections.defaultdict(list)
    count = 0
    for word in string_list:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams[sorted_word].append(word)
    for group in anagrams.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
            if count > 173:
                return False
    return True