def palindromes_between_indices(s):
    sub_string = s[2:5]
    palindromes = set()
    for i in range(len(sub_string)):
        for j in range(i, len(sub_string)):
            sub = sub_string[i:j + 1]
            if sub == sub[::-1]:
                palindromes.add(sub)
    return palindromes