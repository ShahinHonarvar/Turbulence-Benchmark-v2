def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substr = s[3:10].lower()
    result = set()
    for i in range(0, len(substr) - 6):
        for j in range(i + 1, len(substr) - 5):
            for k in range(j + 1, len(substr) - 4):
                for l in range(k + 1, len(substr) - 3):
                    for m in range(l + 1, len(substr) - 2):
                        for n in range(m + 1, len(substr) - 1):
                            for o in range(n + 1, len(substr)):
                                pal = ''.join(sorted(substr[i:o + 1], reverse=True))
                                if set(pal) <= english_letters and len(pal) >= 7:
                                    result.add(pal)
    return result