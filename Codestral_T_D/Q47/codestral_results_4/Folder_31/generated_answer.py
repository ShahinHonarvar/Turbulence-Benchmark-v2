def palindromes_of_specific_lengths(s):
    palindromes = set()
    sub_string = s[11:84]
    for l in range(37, 61):
        for i in range(len(sub_string) - l + 1):
            sub = sub_string[i:i + l]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes