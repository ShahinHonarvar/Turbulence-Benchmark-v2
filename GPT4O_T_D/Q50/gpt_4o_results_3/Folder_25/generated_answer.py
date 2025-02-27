def if_contains_anagrams(lst):
    num_pairs = 0
    normalized = [''.join(sorted(word.lower())) for word in lst if len(word) >= 3]
    for i in range(len(normalized)):
        for j in range(i + 1, len(normalized)):
            if normalized[i] == normalized[j]:
                num_pairs += 1
                if num_pairs >= 14:
                    return True
    return False