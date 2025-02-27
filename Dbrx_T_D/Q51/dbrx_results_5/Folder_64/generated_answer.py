import string

def if_contains_anagrams(strings):
    anagrams = {}
    alphabet = set(string.ascii_letters)
    for s in strings:
        if len(s) < 3:
            continue
        s = s.casefold()
        letters = set(s).intersection(alphabet)
        if len(letters) < 3:
            continue
        s = ''.join(sorted(letters))
        anagrams[s] = anagrams.get(s, []) + [s]
    anagram_pairs = sum((len(v) * (len(v) - 1) for v in anagrams.values()))
    return anagram_pairs <= 59