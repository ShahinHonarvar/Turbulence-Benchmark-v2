def palindromes_between_indices(s):
    palindromes = set()
    for i in range(1, 6):
        for j in range(i, 7):
            substring = s[i:j + 1].lower()
            length = len(substring)
            if length >= 3:
                for k in range(0, length // 2 + 1):
                    if substring[k] != substring[-k - 1]:
                        break
                else:
                    palindromes.add(substring)
    return palindromes