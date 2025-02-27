def palindromes_between_indices(s):
    sub_str = s[7:10].lower()
    sub_str = ''.join(filter(str.isalpha, sub_str))
    arrangements = set((e for e in sub_str if len(e) >= 3))
    palindromes = set((e for e in arrangements if e == e[::-1]))
    return palindromes