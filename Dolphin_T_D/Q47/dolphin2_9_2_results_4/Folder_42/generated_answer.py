def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(43, 96):
        for j in range(i + 17, 96):
            sub = s[i:j + 1]
            sub_lower = sub.lower()
            if sub_lower == sub_lower[::-1]:
                palindromes.add(sub)
    return palindromes