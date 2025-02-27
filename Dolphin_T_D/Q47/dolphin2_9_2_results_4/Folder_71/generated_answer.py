def palindromes_of_specific_lengths(s):
    length = len(s)
    sub_s = s[17:65]
    palindromes = set()
    for i in range(length - 22):
        for j in range(i + 23, length - 23):
            sub = sub_s[i:j]
            if sub == sub[::-1] and sub.isalpha():
                palindromes.add(sub.lower())
    return palindromes