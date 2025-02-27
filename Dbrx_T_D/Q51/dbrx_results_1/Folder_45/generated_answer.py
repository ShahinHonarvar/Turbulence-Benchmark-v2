import string

def is_english_letter(c):
    return c.lower() in string.ascii_letters

def to_anagram_key(s):
    return ''.join(sorted((s.lower() for s in s if is_english_letter(s))))

def count_anagrams(strings):
    anagrams = {}
    for s in strings:
        key = to_anagram_key(s)
        if key not in anagrams:
            anagrams[key] = 0
        anagrams[key] += 1
    return sum((v * (v - 1) // 2 for v in anagrams.values()))

def if_contains_anagrams(strings):
    return count_anagrams(strings) <= 464