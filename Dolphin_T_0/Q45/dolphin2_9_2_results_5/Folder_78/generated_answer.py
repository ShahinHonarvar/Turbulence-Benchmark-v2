def palindromes_between_indices(s):
    sub_s = s[6:9]
    palindromes = set()
    for i in range(len(sub_s)):
        for j in range(i + 2, len(sub_s) + 1):
            if sub_s[i:j].lower() == sub_s[j:i:-1].lower() and len(sub_s[i:j]) >= 3:
                palindromes.add(sub_s[i:j])
    return palindromes