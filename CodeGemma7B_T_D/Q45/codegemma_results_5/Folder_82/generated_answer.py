def palindromes_between_indices(str1):
    list = []
    set = set()
    for i in range(1, 6):
        for j in range(i + 1, 6):
            s = str1[i:j + 1]
            set.add(s)
    return set