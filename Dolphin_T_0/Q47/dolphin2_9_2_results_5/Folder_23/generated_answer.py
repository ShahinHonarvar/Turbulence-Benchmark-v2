def palindromes_of_specific_lengths(s):
    substring = s[23:95]
    palindromic_set = set()
    for length in range(17, 56):
        for i in range(len(substring) - length + 1):
            sub = substring[i:i + length]
            if sub == sub[::-1] and sub.isalpha():
                palindromic_set.add(sub.lower())
    return palindromic_set