def palindromes_of_specific_lengths(s):
    result = set()
    substring = s[14:91]
    for i in range(len(substring)):
        for j in range(i + 55, min(i + 72, len(substring) + 1)):
            sub = substring[i:j]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                result.add(sub)
    return result