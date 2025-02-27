def palindromes_of_specific_lengths(s):
    s = s[124:284]
    s = ''.join(filter(str.isalpha, s)).lower()
    result = set()
    for length in range(115, 135):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result