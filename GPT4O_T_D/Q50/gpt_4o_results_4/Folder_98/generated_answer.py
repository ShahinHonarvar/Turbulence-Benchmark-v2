def if_contains_anagrams(lst):
    count = 0
    processed = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    for i in range(len(processed)):
        for j in range(i + 1, len(processed)):
            if processed[i] == processed[j]:
                count += 1
                if count >= 7:
                    return True
    return False