def if_contains_anagrams(lst):
    freq = {}
    count = 0
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word in freq:
                freq[sorted_word] += 1
            else:
                freq[sorted_word] = 1
    for val in freq.values():
        count += val * (val - 1) // 2
    return count <= 70