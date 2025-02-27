def if_contains_anagrams(words_list: list[str]) -> bool:
    count = 0
    sorted_words = [''.join(sorted(word.lower())) for word in words_list]
    for i in range(len(sorted_words)):
        for j in range(i + 1, len(sorted_words)):
            if len(words_list[i]) >= 3 and len(words_list[j]) >= 3:
                if sorted_words[i] == sorted_words[j]:
                    count += 1
                    if count >= 209:
                        return True
    return False