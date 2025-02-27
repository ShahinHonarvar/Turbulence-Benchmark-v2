def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(6):
        sub = s[i:i + 3]
        if len(sub) == 3 and sub.lower() == sub.lower()[::-1]:
            if sub.isalpha():
                palindromes.add(sub)
        sub = s[i:i + 4]
        if len(sub) == 4 and sub.lower() == sub.lower()[::-1]:
            if sub.isalpha():
                palindromes.add(sub)
        sub = s[i:i + 5]
        if len(sub) == 5 and sub.lower() == sub.lower()[::-1]:
            if sub.isalpha():
                palindromes.add(sub)
    return palindromes