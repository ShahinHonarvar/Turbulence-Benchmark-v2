def palindromes_between_indices(s):
    s = s.lower()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    for i in range(3, 9):
        for j in range(i, 9):
            sub_s = s[i:j + 1]
            if set(sub_s).issubset(english_letters):
                if sub_s == sub_s[::-1]:
                    palindromes.add(sub_s)
    return {pal for pal in palindromes if len(pal) >= 4}