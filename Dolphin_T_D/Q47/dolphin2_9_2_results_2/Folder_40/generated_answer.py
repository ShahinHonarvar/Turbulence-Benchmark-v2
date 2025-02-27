def palindromes_of_specific_lengths(s):
    sub = s[0:6].lower()
    result = set()
    for length in range(3, 6):
        for i in range(len(sub) - length + 1):
            if sub[i:i + length] == sub[i:i + length][::-1] and sub[i:i + length].isalpha():
                result.add(sub[i:i + length])
    return result