def if_contains_anagrams(strings):

    def sorted_lower(s):
        return ''.join(sorted(s.lower()))
    strings = [s for s in strings if len(s) >= 3]
    seen = {}
    count = 0
    for s in strings:
        sorted_s = sorted_lower(s)
        if sorted_s in seen:
            count += seen[sorted_s]
            seen[sorted_s] += 1
        else:
            seen[sorted_s] = 1
        if count >= 18:
            return True
    return False