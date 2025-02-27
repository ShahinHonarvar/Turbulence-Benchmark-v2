def if_contains_anagrams(words):
    count = 0
    normalized_words = [''.join(sorted(word.lower())) for word in words]
    n = len(normalized_words)
    for i in range(n):
        if len(normalized_words[i]) < 3:
            continue
        for j in range(i + 1, n):
            if len(normalized_words[j]) < 3:
                continue
            if normalized_words[i] == normalized_words[j]:
                count += 1
                if count > 38:
                    return False
    return True