def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(39, 95):
        for j in range(i + 14, min(i + 53, 95)):
            sub = s[i:j]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                result.add(sub)
    return result