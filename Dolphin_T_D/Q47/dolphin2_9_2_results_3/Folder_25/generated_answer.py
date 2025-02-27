def palindromes_of_specific_lengths(s):
    s = s[25:85]
    set_palin = set()
    for i in range(30, 47):
        for j in range(i):
            if s[j:j + i].lower() == s[j:j + i][::-1].lower() and s[j:j + i].isalpha():
                set_palin.add(s[j:j + i])
    return set_palin