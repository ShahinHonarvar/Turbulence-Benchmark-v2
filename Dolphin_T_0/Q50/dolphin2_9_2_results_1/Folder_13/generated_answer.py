def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    pair_count = 0
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if sorted(words[i]) == sorted(words[j]):
                pair_count += 1
                if pair_count >= 144:
                    return True
    return False