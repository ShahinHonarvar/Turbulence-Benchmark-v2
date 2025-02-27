def palindromes_between_indices(text):
    text = text[5:7]
    c = text.lower().count
    n = len(text)
    for i in range(n):
        for j in range(i, n):
            for k in range(i, j + 1):
                if c(text[k]) >= 2:
                    n -= c(text[k]) // 2
            if n >= 3:
                s = text[i:j + 1]
                if s == s[::-1]:
                    print(s)
                    return True
    return set()