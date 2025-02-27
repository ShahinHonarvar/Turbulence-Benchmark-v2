def palindromes_of_specific_lengths(s):
    s = s[40:95]
    result = set()
    for l in range(45, 52):
        for i in range(len(s) - l + 1):
            if all((c.isalpha() for c in s[i:i + l])) and s[i:i + l].lower() == s[i:i + l][::-1].lower():
                result.add(s[i:i + l])
    return result