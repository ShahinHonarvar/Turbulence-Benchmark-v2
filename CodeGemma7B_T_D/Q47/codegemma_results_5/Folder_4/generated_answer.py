def palindromes_of_specific_lengths(txt):
    low = 12
    high = 92
    size_min = 17
    size_max = 66
    ps = set()
    for start in range(low, high - size_max + 1):
        for end in range(high, start + size_min - 1, -1):
            word = txt[start:end + 1]
            if word == word.lower():
                ps.add(word)
    return ps