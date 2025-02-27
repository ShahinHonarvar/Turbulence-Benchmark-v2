def palindrome_of_length_n(txt):
    results = set()
    txt = txt.lower()
    for i in range(len(txt)):
        for j in range(i + 1, len(txt)):
            if txt[i] == txt[j] and j - i + 1 == 28:
                results.add(txt[i:j + 1])
    return results