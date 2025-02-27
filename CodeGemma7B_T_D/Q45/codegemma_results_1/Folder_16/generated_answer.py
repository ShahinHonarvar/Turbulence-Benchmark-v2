def palindromes_between_indices(str):
    str = str.lower()
    lst = list(str[6:10])
    lst.sort()
    palindromes = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                for l in range(k + 1, len(lst)):
                    for m in range(l + 1, len(lst)):
                        palindrome = lst[i] + lst[j] + lst[k] + lst[l] + lst[m]
                        palindromes.add(palindrome)
    return palindromes