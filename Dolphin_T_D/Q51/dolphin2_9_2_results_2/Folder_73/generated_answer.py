from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            counter = Counter(word)
            key = ''.join(sorted(counter.keys()))
            if key in anagrams:
                anagrams[key].append(word)
                count += len(anagrams[key])
                if count >= 279:
                    return True
            else:
                anagrams[key] = [word]
    return False