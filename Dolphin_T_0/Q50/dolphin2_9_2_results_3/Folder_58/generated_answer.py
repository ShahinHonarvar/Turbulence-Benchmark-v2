def if_contains_anagrams(words):
    counter = 0
    sorted_words = [''.join(sorted(word.lower())).__str__() for word in words if len(word) >= 3]
    counted_words = {}
    for word in sorted_words:
        if word in counted_words:
            counted_words[word] += 1
            counter += counted_words[word]
        else:
            counted_words[word] = 1
            counter += 1
    return counter >= 411