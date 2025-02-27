from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    d = {}
    for word in strings:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in d:
                d[sorted_word] = Counter(word)
            else:
                count += 1
    return count <= 40