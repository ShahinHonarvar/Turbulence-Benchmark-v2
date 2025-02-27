import itertools

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) < 3:
            continue
        word = word.lower()
        anagrams = set()
        for i in range(len(word) - 2):
            for j in range(i + 2, len(word) + 1):
                substring = word[i:j]
                anagrams.add(tuple(sorted(substring)))
        for ans1 in anagrams:
            for ans2 in anagrams:
                if ans1 == ans2:
                    continue
                count += 1
    return count >= 89