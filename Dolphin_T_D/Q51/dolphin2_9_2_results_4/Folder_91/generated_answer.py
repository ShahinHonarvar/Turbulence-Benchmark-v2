def if_contains_anagrams(l):
    count = 0
    anagram_dict = {}
    for word in l:
        if len(word) < 3:
            continue
        key = ''.join(sorted(word.lower()))
        if key in anagram_dict:
            count += 1
            if count > 88:
                return False
        else:
            anagram_dict[key] = word
    return True if count <= 88 else False