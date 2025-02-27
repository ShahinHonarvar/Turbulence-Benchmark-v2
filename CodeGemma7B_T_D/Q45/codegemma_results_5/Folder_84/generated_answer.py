def palindromes_between_indices(text):
    st = sorted(text[4:10].lower())
    result = set()
    for i in range(len(st) - 2):
        for j in range(i + 2, len(st)):
            result.add(''.join(st[i:j + 1][::-1]))
    return result or {'None'}