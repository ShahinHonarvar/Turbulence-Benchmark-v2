import string

def if_contains_anagrams(strings):
    anagrams = set()
    count = 0
    for s in strings:
        sorted_s = ''.join(sorted(s.lower().translate(str.maketrans('', '', string.punctuation))))
        if len(sorted_s) < 3:
            continue
        if sorted_s in anagrams:
            count += 1
            if count > 392:
                return False
        else:
            anagrams.add(sorted_s)
    return True