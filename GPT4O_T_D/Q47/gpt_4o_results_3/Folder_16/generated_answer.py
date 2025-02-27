def palindromes_of_specific_lengths(s):
    s = s[15:87]
    filtered_s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for length in range(51, 61):
        for i in range(len(filtered_s) - length + 1):
            substring = filtered_s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result