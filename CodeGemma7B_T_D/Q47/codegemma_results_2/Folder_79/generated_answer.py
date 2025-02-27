def palindromes_of_specific_lengths(str1):
    palindromes = set()
    str1 = str1.lower()
    for i in range(1, 8):
        for j in range(i + 1, 8):
            for k in range(i, j + 1):
                if str1[i] == str1[j] and (k - i + 1 == 3 or k - i + 1 == 4):
                    palindromes.add(str1[i:j + 1])
    return palindromes