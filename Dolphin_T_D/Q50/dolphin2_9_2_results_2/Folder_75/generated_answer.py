def if_contains_anagrams(words):
    count = 0
    for word in words:
        if len(word) >= 3:
            for w in words:
                if len(w) >= 3 and sorted(word.lower()) == sorted(w.lower()):
                    count += 1
    return count >= 70