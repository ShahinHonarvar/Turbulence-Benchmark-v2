def if_contains_anagrams(lst):
    count = 0
    processed = set()
    for word in lst:
        word = word.replace(' ', '').lower()
        if word in processed or len(word) < 3:
            continue
        key = ''.join(sorted(word))
        for w in lst:
            if key == ''.join(sorted(w.replace(' ', '').lower())) and word != w:
                count += 1
                if count > 445:
                    return False
                break
        processed.add(word)
    return True