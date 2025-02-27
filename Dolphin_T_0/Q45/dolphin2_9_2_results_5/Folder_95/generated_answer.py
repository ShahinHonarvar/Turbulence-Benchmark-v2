def palindromes_between_indices(s):
    letters_between = s[7:9]
    palindromes = set()
    for p in range(len(letters_between)):
        for q in range(p + 2, len(letters_between) + 1):
            sub = letters_between[p:q]
            str_sub = ''.join(sub)
            if str_sub == str_sub.lower()[::-1] and len(str_sub) >= 3:
                palindromes.add(str_sub)
    return palindromes