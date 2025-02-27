def palindromes_between_indices(s):
    s = ''.join([c for c in s if c.isalpha()])[1:8]
    s = s.lower()
    arr = list(s)
    n = len(arr)
    palindromes = set()
    for i in range(0, n):
        for j in range(i + 1, n):
            arr[i], arr[j] = (arr[j], arr[i])
            pal = ''.join(arr)
            if pal == pal[::-1] and len(pal) >= 6:
                palindromes.add(pal)
            arr[i], arr[j] = (arr[j], arr[i])
    return palindromes