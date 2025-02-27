from collections import Counter

def if_contains_anagrams(strings):
    map = {}
    pairs = 0
    for word in strings:
        if len(word) < 3:
            pass
        else:
            character_count = Counter(word.lower())
            key = ''.join(sorted(character_count.keys()))
            if key not in map:
                map[key] = [word]
            else:
                for anagram in map[key]:
                    if word.lower() == anagram.lower() or word == anagram.lower() or word.lower() == anagram:
                        pass
                    else:
                        pairs += 1
                        map[key].append(word)
    return pairs >= 314