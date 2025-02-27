def palindromes_between_indices(text):
    sub_str = text[1:10]
    eng_let = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    letters = set([c for c in sub_str if c in eng_let])
    if len(''.join(sorted(list(letters)))) < 7:
        return set()
    result = set()
    for length in range(7, len(sub_str) + 1):
        for start_index in range(len(sub_str) - length + 1):
            sub = sub_str[start_index:start_index + length]
            if sub == sub[::-1]:
                sub = ''.join(sorted(list(sub)))
                result.add(sub)
    return result