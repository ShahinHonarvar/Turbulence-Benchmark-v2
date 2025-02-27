def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    count = 0
    sorted_words = [''.join(sorted(word)) for word in lst]
    frequency = {}
    for word in sorted_words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    for freq in frequency.values():
        if freq > 1:
            count += freq * (freq - 1) // 2
            if count >= 75:
                return True
    return False