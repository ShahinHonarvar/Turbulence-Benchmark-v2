def palindromes_of_specific_lengths(s):
    sub_s = s[15:90]
    lower_s = sub_s.lower()
    result = set()
    for length in range(40, 73):
        for i in range(len(lower_s) - length + 1):
            substr = lower_s[i:i + length]
            if substr == substr[::-1] and substr.isalpha():
                result.add(substr)
    return result