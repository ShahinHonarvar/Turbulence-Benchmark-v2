from collections import Counter

def if_contains_anagrams(words):
    count = 0
    seen = set()
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            letter_count = Counter(word)
            for perm in permutations(word):
                perm = ''.join(perm)
                if perm in seen:
                    count += 1
                else:
                    seen.add(perm)
    return count <= 97