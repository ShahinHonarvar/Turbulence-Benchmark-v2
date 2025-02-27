def palindromes_of_specific_lengths(s):
    result = set()
    s = s[130:296]
    for length in range(103, 159):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                result.add(sub)
    return result