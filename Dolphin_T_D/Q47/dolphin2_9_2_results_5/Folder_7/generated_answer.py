def palindromes_of_specific_lengths(s):
    s = s[118:257].lower()
    result = set()
    for length in range(104, 124):
        for i in range(len(s) - length + 1):
            if all((x.isalpha() for x in s[i:i + length])) and s[i:i + length] == s[i:i + length][::-1]:
                result.add(s[i:i + length])
    return result