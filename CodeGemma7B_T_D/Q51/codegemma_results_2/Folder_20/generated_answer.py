def if_contains_anagrams(words):
    counts = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) < 3:
            continue
        if sorted_word not in counts:
            counts[sorted_word] = 0
        counts[sorted_word] += 1
    pairs = 0
    for count in counts.values():
        pairs += count * (count - 1) // 2
    return pairs <= 131