def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(11, 94):
        for length in range(34, 55):
            if i + length - 1 > 93:
                break
            elif s[i:i + length].lower() == s[i:i + length].lower()[::-1]:
                result.add(s[i:i + length])
    return result