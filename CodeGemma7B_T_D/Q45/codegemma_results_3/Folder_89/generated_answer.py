def palindromes_between_indices(text):
    set_of_pal = set()
    for i in range(5, 10):
        for j in range(i + 1, 10):
            for k in range(j + 1, 10):
                for l in range(k + 1, 10):
                    for m in range(l + 1, 10):
                        list_of_letters = [text[i], text[j], text[k], text[l], text[m]]
                        str_of_letters = ''.join(sorted(list_of_letters, key=str.casefold))
                        if str_of_letters in set_of_pal:
                            continue
                        set_of_pal.add(str_of_letters)
    if not set_of_pal:
        return set()
    return set_of_pal