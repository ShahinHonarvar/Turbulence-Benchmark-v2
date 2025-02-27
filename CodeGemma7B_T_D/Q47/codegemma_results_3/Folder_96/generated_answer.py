def palindromes_of_specific_lengths(s):
    res = set()
    for i in range(100, 301):
        for j in range(50, 101):
            for k in range(i - j, i + 1):
                temp = s[k:k + j]
                if temp == temp[::-1] and temp.isalpha():
                    res.add(temp)
    return res