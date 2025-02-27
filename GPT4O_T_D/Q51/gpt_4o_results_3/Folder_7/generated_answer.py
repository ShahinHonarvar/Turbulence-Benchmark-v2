def if_contains_anagrams(words):
    counts = {}
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            if sorted_word in counts:
                counts[sorted_word] += 1
            else:
                counts[sorted_word] = 1
    pair_count = 0
    for count in counts.values():
        if count > 1:
            pair_count += count * (count - 1) // 2
        if pair_count > 445:
            return False
    return True