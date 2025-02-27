def palindromes_of_specific_lengths(s):
    s = s[25:91]
    result = set()
    for length in range(27, 59):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            lower_substring = substring.lower()
            if lower_substring == lower_substring[::-1] and lower_substring.isalpha():
                result.add(substring)
    return result