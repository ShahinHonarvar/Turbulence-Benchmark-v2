def palindromes_of_specific_lengths(s):
    s = s[100:296]
    result = set()
    for length in range(136, 161):
        for i in range(len(s) - length + 1):
            sub = s[i:i + length]
            if sub.lower() == sub.lower()[::-1] and sub.isalpha():
                result.add(sub)
    return result