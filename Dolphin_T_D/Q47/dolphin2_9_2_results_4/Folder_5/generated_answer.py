def palindromes_of_specific_lengths(s):
    substring = s[63:71]
    palindromes = set()
    for i in range(63, 71):
        for j in range(i + 4, min(i + 5, 71)):
            sub = substring[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes