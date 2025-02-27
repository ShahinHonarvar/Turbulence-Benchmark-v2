def palindromes_of_specific_lengths(s):
    sub_string = s[40:95]
    palindromes = set()
    for i in range(45, 52):
        for j in range(0, len(sub_string) - i + 1):
            sub = sub_string[j:j + i]
            if sub == sub[::-1]:
                palindromes.add(sub.lower())
    return palindromes