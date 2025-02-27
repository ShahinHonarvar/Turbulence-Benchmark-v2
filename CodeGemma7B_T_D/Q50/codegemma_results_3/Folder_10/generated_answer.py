def if_contains_anagrams(words):
    filtered_words = [word for word in words if len(word) >= 3]
    for i in range(len(filtered_words)):
        for j in range(i + 1, len(filtered_words)):
            if sorted(filtered_words[i].lower()) == sorted(filtered_words[j].lower()):
                return True
    return False