def if_contains_anagrams(word_list: list[str]) -> bool:
    count = 0
    sorted_words = [''.join(sorted(word.lower())) for word in word_list]
    for i in range(len(sorted_words)):
        for j in range(i + 1, len(sorted_words)):
            if sorted_words[i] == sorted_words[j] and len(word_list[i]) >= 3:
                count += 1
                if count >= 178:
                    return True
    return False