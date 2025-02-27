def palindromes_between_indices(s):
    palindromes = set()
    sub = s[4:9].lower()
    for i in range(len(sub)):
        for j in range(i + 2, len(sub) + 1):
            sub_pal = sub[i:j]
            if sub_pal == sub_pal[::-1]:
                if len(sub_pal) >= 3:
                    palindromes.add(sub_pal)
    return palindromes