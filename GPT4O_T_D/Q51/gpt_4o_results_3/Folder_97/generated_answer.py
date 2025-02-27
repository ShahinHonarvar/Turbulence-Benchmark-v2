def if_contains_anagrams(words):
    pairs_count = 0
    processed = []
    for word in words:
        lower_word = ''.join(filter(str.isalpha, word)).lower()
        if len(lower_word) >= 3:
            sorted_word = ''.join(sorted(lower_word))
            processed.append(sorted_word)
    for i in range(len(processed)):
        for j in range(i + 1, len(processed)):
            if processed[i] == processed[j]:
                pairs_count += 1
                if pairs_count > 18:
                    return False
    return True