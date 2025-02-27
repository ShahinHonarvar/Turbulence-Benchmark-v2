import collections

def if_contains_anagrams(strings):
    count = 0
    pairs = set()
    for word in strings:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            if sorted_word in pairs:
                pairs.remove(sorted_word)
                count += 1
            else:
                pairs.add(sorted_word)
    return count <= 366