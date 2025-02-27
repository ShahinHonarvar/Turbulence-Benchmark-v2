def if_contains_anagrams(words_list: list[str]) -> bool:
    count = 0
    sorted_words = [''.join(sorted(word.lower())) for word in words_list]
    for i in range(len(sorted_words)):
        for j in range(i + 1, len(sorted_words)):
            if sorted_words[i] == sorted_words[j] and len(sorted_words[i]) >= 3:
                count += 1
                if count >= 312:
                    return True
    return False