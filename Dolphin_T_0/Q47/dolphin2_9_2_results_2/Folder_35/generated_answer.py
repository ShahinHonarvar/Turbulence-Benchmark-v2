def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(34, 91):
        for j in range(i + 14, 91):
            sub_string = s[i:j].lower()
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string)
    if len(palindromes) > 0:
        for p in palindromes:
            if not p.isalpha():
                palindromes.remove(p)
    return palindromes