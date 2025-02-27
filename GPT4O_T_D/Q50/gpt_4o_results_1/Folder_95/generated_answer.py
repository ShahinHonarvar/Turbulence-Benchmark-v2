def if_contains_anagrams(words):
    counts = {}
    for word in words:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in counts:
                counts[sorted_word] += 1
            else:
                counts[sorted_word] = 1
    total_pairs = 0
    for _, count in counts.items():
        if count > 1:
            total_pairs += count * (count - 1) // 2
        if total_pairs >= 93:
            return True
    return False