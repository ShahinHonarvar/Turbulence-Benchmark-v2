def if_contains_anagrams(words):
    sorted_words = [''.join(sorted(word.lower())) for word in words if len(word) >= 3]
    count = len(sorted_words) - len(set(sorted_words))
    if count >= 4:
        return True
    else:
        return False