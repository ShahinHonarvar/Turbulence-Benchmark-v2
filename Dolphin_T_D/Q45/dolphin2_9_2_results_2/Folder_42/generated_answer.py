def palindromes_between_indices(s):
    s = s[6:10]
    arr = list(s.lower())
    palindromes = set()
    for i in range(len(arr)):
        for j in range(i + 2, len(arr) + 1):
            pal = ''.join(arr[i:j])
            if pal == pal[::-1]:
                palindromes.add(pal)
    return palindromes