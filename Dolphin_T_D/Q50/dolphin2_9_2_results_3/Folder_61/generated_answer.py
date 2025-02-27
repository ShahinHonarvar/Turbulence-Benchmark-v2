def if_contains_anagrams(words):
    count = 0
    for word in words:
        if len(word) > 2:
            for other_word in words:
                if sorted(word.lower()) == sorted(other_word.lower()):
                    count += 1
    return count >= 8