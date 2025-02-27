def if_contains_anagrams(strings):
    strings = [''.join(filter(str.isalpha, s)).lower() for s in strings if len(''.join(filter(str.isalpha, s)).lower()) >= 3]
    anagrams = {}
    count = 0
    for s in strings:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
            count += anagrams[sorted_s]
        else:
            anagrams[sorted_s] = 1
    return count <= 72