def if_contains_anagrams(lst):
    freq = {}
    for wrd in lst:
        key = ''.join(sorted(wrd.lower()))
        if len(key) >= 3:
            if key in freq:
                freq[key] += 1
            else:
                freq[key] = 1
    pairs_count = 0
    for k, v in freq.items():
        if v > 1:
            pairs_count += v * (v - 1) // 2
    return pairs_count >= 219