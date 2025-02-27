from collections import Counter

def if_contains_anagrams(words):
    count = 0
    for word in words:
        if len(word) >= 3:
            counter = Counter(word.lower())
            for other_word in words:
                if len(other_word) >= 3 and other_word.lower() != word.lower():
                    if Counter(other_word.lower()) == counter:
                        count += 1
    return count >= 39