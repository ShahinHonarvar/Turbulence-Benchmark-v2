def palindromes_between_indices(s):
    s = s.lower()
    sub_str = s[4:7]
    sub_str = ''.join((e for e in sub_str if e.isalpha()))
    palindromes = set()
    for i in range(len(sub_str)):
        for j in range(i + 1, len(sub_str)):
            if sub_str[i] == sub_str[j]:
                palindromes.add(sub_str[i:j + 1])
    return palindromes