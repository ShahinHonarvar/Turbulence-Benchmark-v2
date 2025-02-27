def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    normalized = [normalize(s) for s in strings if len(s) >= 3]
    seen = {}
    for word in normalized:
        if word in seen:
            count += seen[word]
            if count > 50:
                return False
            seen[word] += 1
        else:
            seen[word] = 1
    return True