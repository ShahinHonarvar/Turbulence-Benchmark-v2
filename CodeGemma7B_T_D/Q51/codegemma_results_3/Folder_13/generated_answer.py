def if_contains_anagrams(strings):
    seen = {}
    for word in strings:
        word = ''.join(sorted(word.lower()))
        if word not in seen:
            seen[word] = 0
        seen[word] += 1
        if seen[word] == 55:
            return False
    return True