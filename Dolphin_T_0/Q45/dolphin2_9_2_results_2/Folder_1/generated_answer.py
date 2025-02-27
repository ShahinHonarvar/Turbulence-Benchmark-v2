def palindromes_between_indices(s):
    sub_s = s[4:8]
    sub_s = ''.join(filter(str.isalpha, sub_s)).lower()
    if len(set(sub_s)) < 5:
        return set()
    palindromes = set()
    for i in range(5, len(sub_s) + 1):
        for j in range(len(sub_s) - i + 1):
            if sub_s[j:j + i] == sub_s[j:j + i][::-1]:
                palindromes.add(sub_s[j:j + i])
    return palindromes