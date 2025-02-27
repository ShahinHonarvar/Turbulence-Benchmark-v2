def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for i in range(100, 201):
        for length in range(5, 11):
            if i + length <= 200 and s[i:i + length] == s[i:i + length][::-1]:
                result.add(s[i:i + length])
    return result