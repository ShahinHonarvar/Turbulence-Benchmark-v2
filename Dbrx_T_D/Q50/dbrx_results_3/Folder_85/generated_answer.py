import re

def if_contains_anagrams(words):
    words = [re.sub('[^\\\\w]', '', word).lower() for word in words]
    words = [word for word in words if len(word) >= 3]
    anagrams = [word for word in words if ''.join(sorted(word)) in pairs]
    pairs = [(x, y) for x in words for y in words if x != y and ''.join(sorted(x)) == ''.join(sorted(y))]
    return len(pairs) >= 73