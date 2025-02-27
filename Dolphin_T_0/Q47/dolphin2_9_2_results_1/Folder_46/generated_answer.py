def palindromes_of_specific_lengths(s):
    result = set()
    s = s[10:97]
    for length in range(29, 63):
        for i in range(len(s) - length + 1):
            subS = s[i:i + length]
            if subS.lower() == subS.lower()[::-1]:
                result.add(subS)
    return result