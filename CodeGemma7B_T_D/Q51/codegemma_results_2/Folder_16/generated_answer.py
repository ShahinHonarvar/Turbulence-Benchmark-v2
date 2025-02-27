def if_contains_anagrams(list):
    seen = {}
    count = 0
    for word in list:
        word = ''.join(sorted(word.lower()))
        if word not in seen:
            seen[word] = 0
        seen[word] += 1
        count += 1
        if count > 24:
            return False
    return True