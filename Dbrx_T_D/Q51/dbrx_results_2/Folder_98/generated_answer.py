import collections

def is_english(s):
    return all((ord('a') <= ord(c.lower()) <= ord('z') for c in s))

def is_anagram(s, t):
    return sorted(s.lower()) == sorted(t.lower())

def count_anagrams(words):
    words = [word for word in words if len(word) >= 3 and is_english(word)]
    anagrams = collections.defaultdict(list)
    for word in words:
        anagrams[''.join(sorted(word.lower()))].append(word)
    return sum((len(group) > 1 for group in anagrams.values()))

def if_contains_anagrams(words):
    return count_anagrams(words) <= 46