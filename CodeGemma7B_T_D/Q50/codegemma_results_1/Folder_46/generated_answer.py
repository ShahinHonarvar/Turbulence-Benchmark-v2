def if_contains_anagrams(list_of_strings):
    sorted_words = [sorted(word.lower()) for word in list_of_strings]
    pairs_count = 0
    for i in range(len(sorted_words)):
        for j in range(i + 1, len(sorted_words)):
            if sorted_words[i] == sorted_words[j]:
                pairs_count += 1
    return pairs_count >= 38