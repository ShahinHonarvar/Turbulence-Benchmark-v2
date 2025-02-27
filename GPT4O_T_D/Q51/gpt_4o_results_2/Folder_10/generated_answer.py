from collections import Counter

def if_contains_anagrams(lst):
    pairs_count = 0
    processed = []
    for word in lst:
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word.lower()))
        if sorted_word in processed:
            continue
        processed.append(sorted_word)
        word_count = Counter((lst.count(w) for w in lst if ''.join(sorted(w.lower())) == sorted_word and len(w) >= 3))
        for count in word_count.values():
            if count > 1:
                pairs_count += count * (count - 1) // 2
        if pairs_count > 21:
            return False
    return True