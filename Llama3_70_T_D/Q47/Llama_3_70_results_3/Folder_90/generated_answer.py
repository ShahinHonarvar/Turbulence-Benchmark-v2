def palindromes_of_specific_lengths(s):
    s = s.lower()
    substr = s[106:281]
    pals = set()
    for i in range(len(substr)):
        for j in range(i + 136, min(i + 152, len(substr) + 1)):
            sub = substr[i:j]
            if sub == sub[::-1] and sub.isalpha():
                pals.add(sub)
    return pals