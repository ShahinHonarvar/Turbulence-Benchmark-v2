from collections import Counter

def if_contains_anagrams(strings):
    pairs = 0
    for string in strings:
        if len(string) >= 3:
            key = ''.join(sorted(Counter(string).lower().elements()))
            pairs += sum((1 for s in strings if len(s) >= 3 and ''.join(sorted(Counter(s).lower().elements())) == key))
            if pairs >= 153:
                return True
    return False