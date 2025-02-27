def palindromes_between_indices(text):
    palindromes = set()
    for i in range(5, 8):
        for j in range(5, 8):
            if i == j:
                continue
            for k in range(5, 8):
                if i == k or j == k:
                    continue
                for l in range(5, 8):
                    if i == l or j == l or k == l:
                        continue
                    words_str = ''
                    words = [i, j, k, l]
                    for word in words:
                        words_str += text[word]
                    if words_str == words_str[::-1]:
                        palindromes.add(words_str)
    return palindromes