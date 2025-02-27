def palindromes_between_indices(s):
    sub_string = s[4:6].lower()
    palindromes = set()
    for i in range(len(sub_string)):
        for j in range(i + 2, len(sub_string) + 1):
            sub = sub_string[i:j]
            if sub == sub[::-1] and len(sub) >= 3:
                palindromes.add(sub)
    return palindromes