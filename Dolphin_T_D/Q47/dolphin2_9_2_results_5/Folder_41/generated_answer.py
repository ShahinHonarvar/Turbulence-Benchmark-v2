def palindromes_of_specific_lengths(s):
    substring = s[1:8].lower()
    pals = set()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            if substring[i:j] == substring[i:j][::-1] and len(substring[i:j]) in [3, 4]:
                pals.add(substring[i:j])
    return pals