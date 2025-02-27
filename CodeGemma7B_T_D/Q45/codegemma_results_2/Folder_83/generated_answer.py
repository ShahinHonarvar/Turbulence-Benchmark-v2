def palindromes_between_indices(text):
    text = text.lower()
    set_of_palindromes = set()
    substring = text[2:10]
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            for k in range(j + 1, len(substring)):
                for l in range(k + 1, len(substring)):
                    for m in range(l + 1, len(substring)):
                        if substring[i] != substring[j] and substring[j] != substring[k] and (substring[k] != substring[l]) and (substring[l] != substring[m]):
                            if substring[i] != substring[m] and substring[j] != substring[l] and (substring[k] != substring[i]) and (substring[l] != substring[j]):
                                new_substring = substring[i] + substring[j] + substring[k] + substring[l] + substring[m]
                                set_of_palindromes.add(new_substring)
    return set_of_palindromes